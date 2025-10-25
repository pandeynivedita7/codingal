#!/usr/bin/env python3
"""
YOLO Baseline CNN Detection Model
Lightweight YOLO implementation for object detection training on MS-COCO or CityPersons
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms as transforms
from torchvision.datasets import CocoDetection
import numpy as np
import cv2
from PIL import Image
import os
import json
from typing import List, Tuple, Dict, Optional
import matplotlib.pyplot as plt
import time

class YOLOv8nBackbone(nn.Module):
    """Lightweight YOLOv8 nano backbone network"""
    
    def __init__(self, in_channels=3):
        super().__init__()
        
        # Stem
        self.stem = nn.Sequential(
            nn.Conv2d(in_channels, 16, 3, 2, 1, bias=False),
            nn.BatchNorm2d(16),
            nn.SiLU(inplace=True)
        )
        
        # Stage 1
        self.stage1 = nn.Sequential(
            nn.Conv2d(16, 32, 3, 2, 1, bias=False),
            nn.BatchNorm2d(32),
            nn.SiLU(inplace=True),
            self._make_c2f_block(32, 32, 1)
        )
        
        # Stage 2
        self.stage2 = nn.Sequential(
            nn.Conv2d(32, 64, 3, 2, 1, bias=False),
            nn.BatchNorm2d(64),
            nn.SiLU(inplace=True),
            self._make_c2f_block(64, 64, 2)
        )
        
        # Stage 3
        self.stage3 = nn.Sequential(
            nn.Conv2d(64, 128, 3, 2, 1, bias=False),
            nn.BatchNorm2d(128),
            nn.SiLU(inplace=True),
            self._make_c2f_block(128, 128, 2)
        )
        
        # Stage 4
        self.stage4 = nn.Sequential(
            nn.Conv2d(128, 256, 3, 2, 1, bias=False),
            nn.BatchNorm2d(256),
            nn.SiLU(inplace=True),
            self._make_c2f_block(256, 256, 1)
        )
        
    def _make_c2f_block(self, in_ch, out_ch, n_blocks):
        """Create C2f block (Cross Stage Partial with 2 convolutions)"""
        layers = []
        for i in range(n_blocks):
            layers.append(nn.Sequential(
                nn.Conv2d(in_ch if i == 0 else out_ch, out_ch, 1, bias=False),
                nn.BatchNorm2d(out_ch),
                nn.SiLU(inplace=True),
                nn.Conv2d(out_ch, out_ch, 3, 1, 1, bias=False),
                nn.BatchNorm2d(out_ch),
                nn.SiLU(inplace=True)
            ))
        return nn.Sequential(*layers)
    
    def forward(self, x):
        x = self.stem(x)
        x1 = self.stage1(x)    # 1/4
        x2 = self.stage2(x1)   # 1/8
        x3 = self.stage3(x2)   # 1/16
        x4 = self.stage4(x3)   # 1/32
        return x2, x3, x4  # Multi-scale features

class YOLODetectionHead(nn.Module):
    """YOLO detection head for object detection"""
    
    def __init__(self, in_channels, num_classes=80, num_anchors=3):
        super().__init__()
        self.num_classes = num_classes
        self.num_anchors = num_anchors
        
        # Detection outputs: x, y, w, h, objectness, classes
        self.out_channels = num_anchors * (5 + num_classes)
        
        self.conv = nn.Sequential(
            nn.Conv2d(in_channels, in_channels, 3, 1, 1, bias=False),
            nn.BatchNorm2d(in_channels),
            nn.SiLU(inplace=True),
            nn.Conv2d(in_channels, self.out_channels, 1)
        )
        
    def forward(self, x):
        return self.conv(x)

class YOLOv8n(nn.Module):
    """Lightweight YOLOv8 nano model"""
    
    def __init__(self, num_classes=80):
        super().__init__()
        self.num_classes = num_classes
        
        # Backbone
        self.backbone = YOLOv8nBackbone()
        
        # Neck (FPN-like structure)
        self.neck = nn.ModuleDict({
            'up1': nn.Upsample(scale_factor=2, mode='nearest'),
            'conv1': nn.Sequential(
                nn.Conv2d(256 + 128, 128, 1, bias=False),
                nn.BatchNorm2d(128),
                nn.SiLU(inplace=True)
            ),
            'up2': nn.Upsample(scale_factor=2, mode='nearest'),
            'conv2': nn.Sequential(
                nn.Conv2d(128 + 64, 64, 1, bias=False),
                nn.BatchNorm2d(64),
                nn.SiLU(inplace=True)
            )
        })
        
        # Detection heads
        self.heads = nn.ModuleList([
            YOLODetectionHead(64, num_classes),   # P3/8
            YOLODetectionHead(128, num_classes),  # P4/16
            YOLODetectionHead(256, num_classes)   # P5/32
        ])
        
        # Initialize weights
        self._initialize_weights()
        
    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
    
    def forward(self, x):
        # Backbone
        p3, p4, p5 = self.backbone(x)
        
        # Neck (top-down pathway)
        x = self.neck['up1'](p5)
        x = torch.cat([x, p4], dim=1)
        p4_out = self.neck['conv1'](x)
        
        x = self.neck['up2'](p4_out)
        x = torch.cat([x, p3], dim=1)
        p3_out = self.neck['conv2'](x)
        
        # Detection heads
        outputs = [
            self.heads[0](p3_out),  # Small objects
            self.heads[1](p4_out),  # Medium objects  
            self.heads[2](p5)       # Large objects
        ]
        
        return outputs

class YOLOLoss(nn.Module):
    """YOLO loss function combining classification, localization, and objectness losses"""
    
    def __init__(self, num_classes=80):
        super().__init__()
        self.num_classes = num_classes
        self.bce_loss = nn.BCEWithLogitsLoss()
        self.mse_loss = nn.MSELoss()
        
    def forward(self, predictions, targets):
        # Simplified loss calculation
        # In practice, you'd implement proper anchor matching and loss computation
        total_loss = 0
        
        for pred in predictions:
            # Placeholder loss - implement proper YOLO loss here
            batch_size = pred.size(0)
            total_loss += torch.mean(pred ** 2)  # Simplified for demonstration
            
        return total_loss

class CocoDatasetCustom(Dataset):
    """Custom COCO dataset for YOLO training"""
    
    def __init__(self, root, annFile, transform=None, img_size=640):
        self.root = root
        self.transform = transform
        self.img_size = img_size
        
        # Load COCO annotations
        with open(annFile, 'r') as f:
            self.coco_data = json.load(f)
        
        self.images = self.coco_data['images']
        self.annotations = self.coco_data['annotations']
        
        # Create image_id to annotations mapping
        self.img_to_anns = {}
        for ann in self.annotations:
            img_id = ann['image_id']
            if img_id not in self.img_to_anns:
                self.img_to_anns[img_id] = []
            self.img_to_anns[img_id].append(ann)
    
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        img_info = self.images[idx]
        img_path = os.path.join(self.root, img_info['file_name'])
        
        # Load image
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Get annotations
        img_id = img_info['id']
        anns = self.img_to_anns.get(img_id, [])
        
        # Convert to PIL for transforms
        image = Image.fromarray(image)
        
        if self.transform:
            image = self.transform(image)
        
        # Create dummy targets (implement proper target formatting)
        targets = torch.zeros(len(anns), 5)  # [class, x, y, w, h]
        
        return image, targets

class YOLOTrainer:
    """YOLO model trainer"""
    
    def __init__(self, model, device='cuda' if torch.cuda.is_available() else 'cpu'):
        self.model = model.to(device)
        self.device = device
        self.criterion = YOLOLoss()
        self.optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.0005)
        self.scheduler = optim.lr_scheduler.StepLR(self.optimizer, step_size=10, gamma=0.1)
        
    def train_epoch(self, dataloader):
        """Train for one epoch"""
        self.model.train()
        total_loss = 0
        
        for batch_idx, (images, targets) in enumerate(dataloader):
            images = images.to(self.device)
            targets = targets.to(self.device)
            
            # Forward pass
            outputs = self.model(images)
            loss = self.criterion(outputs, targets)
            
            # Backward pass
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
            
            total_loss += loss.item()
            
            if batch_idx % 100 == 0:
                print(f'Batch {batch_idx}, Loss: {loss.item():.4f}')
        
        return total_loss / len(dataloader)
    
    def validate(self, dataloader):
        """Validate the model"""
        self.model.eval()
        total_loss = 0
        
        with torch.no_grad():
            for images, targets in dataloader:
                images = images.to(self.device)
                targets = targets.to(self.device)
                
                outputs = self.model(images)
                loss = self.criterion(outputs, targets)
                total_loss += loss.item()
        
        return total_loss / len(dataloader)
    
    def train(self, train_loader, val_loader, epochs=100):
        """Full training loop"""
        train_losses = []
        val_losses = []
        
        for epoch in range(epochs):
            print(f'\nEpoch {epoch+1}/{epochs}')
            
            # Train
            train_loss = self.train_epoch(train_loader)
            train_losses.append(train_loss)
            
            # Validate
            val_loss = self.validate(val_loader)
            val_losses.append(val_loss)
            
            # Update learning rate
            self.scheduler.step()
            
            print(f'Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}')
            
            # Save checkpoint
            if (epoch + 1) % 10 == 0:
                self.save_checkpoint(f'yolo_checkpoint_epoch_{epoch+1}.pth')
        
        return train_losses, val_losses
    
    def save_checkpoint(self, path):
        """Save model checkpoint"""
        torch.save({
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict(),
            'scheduler_state_dict': self.scheduler.state_dict()
        }, path)
        print(f'Checkpoint saved: {path}')

def create_data_loaders(data_root, ann_file, batch_size=16, img_size=640):
    """Create train and validation data loaders"""
    
    # Data transforms
    transform = transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                           std=[0.229, 0.224, 0.225])
    ])
    
    # Dataset
    dataset = CocoDatasetCustom(data_root, ann_file, transform=transform, img_size=img_size)
    
    # Split dataset (80-20 split)
    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])
    
    # Data loaders
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=4)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=4)
    
    return train_loader, val_loader

def main():
    """Main training function"""
    
    # Configuration
    config = {
        'num_classes': 80,  # COCO classes
        'img_size': 640,
        'batch_size': 16,
        'epochs': 100,
        'data_root': '/path/to/coco/images',  # Update this path
        'ann_file': '/path/to/coco/annotations.json'  # Update this path
    }
    
    # Create model
    print("Creating YOLOv8n model...")
    model = YOLOv8n(num_classes=config['num_classes'])
    
    # Model summary
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Total parameters: {total_params:,}")
    print(f"Trainable parameters: {trainable_params:,}")
    
    # Create data loaders (commented out - requires actual COCO dataset)
    # train_loader, val_loader = create_data_loaders(
    #     config['data_root'], 
    #     config['ann_file'],
    #     config['batch_size'],
    #     config['img_size']
    # )
    
    # Create trainer
    trainer = YOLOTrainer(model)
    
    print("YOLOv8n model created successfully!")
    print("\nTo train the model:")
    print("1. Download MS-COCO dataset")
    print("2. Update data_root and ann_file paths")
    print("3. Uncomment the data loader creation")
    print("4. Run: trainer.train(train_loader, val_loader, epochs=100)")
    
    # Example inference (with dummy data)
    model.eval()
    dummy_input = torch.randn(1, 3, 640, 640)
    with torch.no_grad():
        outputs = model(dummy_input)
        print(f"\nModel output shapes:")
        for i, out in enumerate(outputs):
            print(f"Scale {i+1}: {out.shape}")

if __name__ == "__main__":
    main()
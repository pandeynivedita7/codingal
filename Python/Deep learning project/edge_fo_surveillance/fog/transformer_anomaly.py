import torch
import torch.nn as nn

class TransformerAnomaly(nn.Module):
    def __init__(self, feature_dim=16, heads=4):
        super().__init__()
        self.encoder = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model=feature_dim, nhead=heads),
            num_layers=2
        )
        self.fc = nn.Linear(feature_dim, 1)

    def forward(self, x):
        z = self.encoder(x)
        return torch.sigmoid(self.fc(z[-1]))

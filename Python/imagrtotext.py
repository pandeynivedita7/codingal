"""
Image Restoration (Inpainting) Script for VSCode
Uses: huggingface diffusers + Stable Diffusion inpainting
Output: restored PNG (same size), removes tears/scratches while keeping undamaged areas untouched.

Installation:
    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
    pip install diffusers transformers accelerate safetensors huggingface_hub opencv-python pillow
"""

import os
import argparse
from pathlib import Path
from huggingface_hub import login
from PIL import Image
import numpy as np
import cv2
import torch
from diffusers import StableDiffusionInpaintPipeline

# Configuration
HF_TOKEN = "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"  # Replace with your token
MODEL_ID = "stabilityai/stable-diffusion-2-inpainting"

def auto_mask_from_image(pil_image, threshold=30, debug=False):
    """
    Create a mask image that highlights likely scratches/tears/blemishes.
    
    Args:
        pil_image: PIL Image object
        threshold: Edge detection threshold (lower=more sensitive)
        debug: If True, save intermediate debug images
    
    Returns:
        PIL mask (mode 'L') where white (255) is the region to inpaint and black (0) is area to keep.
    """
    # Convert to OpenCV BGR
    img = np.array(pil_image.convert("RGB"))
    bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Convert to gray and increase contrast a bit
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    
    # Use high-pass / Laplacian to highlight edges
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    lap = np.absolute(lap)
    lap = np.uint8(255 * (lap / lap.max()))

    # Morphological operations to connect lines and remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    lap = cv2.medianBlur(lap, 3)
    _, th = cv2.threshold(lap, threshold, 255, cv2.THRESH_BINARY)
    th = cv2.dilate(th, kernel, iterations=1)
    th = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Also detect very bright / very dark spots (common with scratches)
    _, bright = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    _, dark = cv2.threshold(gray, 15, 255, cv2.THRESH_BINARY_INV)
    hair_like = cv2.bitwise_or(bright, th)
    hair_like = cv2.bitwise_or(hair_like, dark)

    # Remove small islands (noise)
    contours, _ = cv2.findContours(hair_like, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros_like(gray)
    min_area = max(3, (img.shape[0] * img.shape[1]) // 20000)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >= min_area:
            cv2.drawContours(mask, [cnt], -1, 255, thickness=cv2.FILLED)

    # Blur the mask a bit so inpaint blends smoothly
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    mask = (mask > 127).astype(np.uint8) * 255

    if debug:
        # Save intermediate steps
        cv2.imwrite("debug_1_gray.png", gray)
        cv2.imwrite("debug_2_edges.png", th)
        cv2.imwrite("debug_3_mask.png", mask)
        print("Debug images saved: debug_1_gray.png, debug_2_edges.png, debug_3_mask.png")

    return Image.fromarray(mask).convert("L")


def load_pipeline(device=None):
    """Load the Stable Diffusion inpainting pipeline."""
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    
    print(f"Using device: {device}")
    
    # Login to Hugging Face
    if HF_TOKEN:
        login(HF_TOKEN)
    
    torch_dtype = torch.float16 if device == "cuda" else torch.float32
    
    print("Loading inpainting pipeline (this may take a minute)...")
    pipe = StableDiffusionInpaintPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch_dtype,
        safety_checker=None,
        variant="fp16" if device == "cuda" else None,
        use_safetensors=True
    )
    pipe = pipe.to(device)
    
    # Enable memory optimizations
    if device == "cuda":
        pipe.enable_attention_slicing()
    
    return pipe, device


def restore_image(input_path, output_path=None, mask_path=None, 
                  prompt=None, num_steps=50, guidance_scale=7.5,
                  auto_mask_threshold=30, debug=False):
    """
    Restore a damaged image using inpainting.
    
    Args:
        input_path: Path to the damaged image
        output_path: Path to save the restored image (default: adds '_restored' to input filename)
        mask_path: Path to manual mask image (white=repair area). If None, auto-generates mask
        prompt: Custom inpainting prompt. If None, uses default restoration prompt
        num_steps: Number of inference steps (more=better quality but slower)
        guidance_scale: How closely to follow the prompt (7.5 is good default)
        auto_mask_threshold: Threshold for automatic mask generation (lower=more sensitive)
        debug: Save debug images showing mask generation process
    
    Returns:
        Path to the restored image
    """
    # Load pipeline
    pipe, device = load_pipeline()
    
    # Load input image
    print(f"Loading image: {input_path}")
    orig_img = Image.open(input_path).convert("RGBA")
    print(f"Image size: {orig_img.size}")
    
    # Generate or load mask
    if mask_path:
        print(f"Loading manual mask: {mask_path}")
        mask = Image.open(mask_path).convert("L")
        mask = mask.resize(orig_img.size)
    else:
        print("Generating automatic mask...")
        mask = auto_mask_from_image(orig_img.convert("RGB"), 
                                    threshold=auto_mask_threshold, 
                                    debug=debug)
    
    # Save mask for inspection
    mask_save_path = str(Path(input_path).with_suffix('')) + "_mask.png"
    mask.save(mask_save_path)
    print(f"Mask saved to: {mask_save_path}")
    
    # Prepare images for pipeline
    init_image = orig_img.convert("RGB")
    mask_image = mask.resize(init_image.size).convert("L")
    
    # Default prompt
    if prompt is None:
        prompt = (
            "Restore the damaged areas of the photo realistically: remove scratches, tears, dust and blemishes. "
            "Preserve original colors, lighting, and texture in undamaged regions."
        )
    
    print("Running inpainting... this may take 30-120 seconds")
    print(f"Prompt: {prompt}")
    
    # Run inpainting
    result = pipe(
        prompt=prompt,
        image=init_image,
        mask_image=mask_image,
        num_inference_steps=num_steps,
        guidance_scale=guidance_scale,
        strength=1.0
    )
    
    restored = result.images[0].convert("RGBA")
    
    # Preserve original alpha channel if present
    if orig_img.mode == "RGBA":
        orig_alpha = orig_img.split()[3]
        restored.putalpha(orig_alpha)
    
    # Save output
    if output_path is None:
        output_path = str(Path(input_path).with_suffix('')) + "_restored.png"
    
    restored.save(output_path)
    print(f"✓ Restored image saved to: {output_path}")
    
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Restore damaged images using AI inpainting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Basic usage with auto-generated mask
    python image_restoration.py damaged_photo.jpg
    
    # Use custom mask (white areas will be repaired)
    python image_restoration.py damaged_photo.jpg --mask my_mask.png
    
    # Specify output path
    python image_restoration.py damaged_photo.jpg --output restored_photo.png
    
    # Adjust mask sensitivity (lower=more sensitive to scratches)
    python image_restoration.py damaged_photo.jpg --threshold 20
    
    # High quality restoration (slower)
    python image_restoration.py damaged_photo.jpg --steps 100 --guidance 9.0
    
    # Debug mode (saves intermediate mask generation steps)
    python image_restoration.py damaged_photo.jpg --debug
        """
    )
    
    parser.add_argument("input", help="Path to damaged image")
    parser.add_argument("-o", "--output", help="Output path (default: input_restored.png)")
    parser.add_argument("-m", "--mask", help="Path to manual mask image (white=repair area)")
    parser.add_argument("-p", "--prompt", help="Custom inpainting prompt")
    parser.add_argument("-s", "--steps", type=int, default=50, 
                       help="Number of inference steps (default: 50)")
    parser.add_argument("-g", "--guidance", type=float, default=7.5,
                       help="Guidance scale (default: 7.5)")
    parser.add_argument("-t", "--threshold", type=int, default=30,
                       help="Auto-mask threshold, lower=more sensitive (default: 30)")
    parser.add_argument("-d", "--debug", action="store_true",
                       help="Save debug images showing mask generation")
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.exists(args.input):
        print(f"Error: Input file not found: {args.input}")
        return 1
    
    # Restore image
    try:
        restore_image(
            input_path=args.input,
            output_path=args.output,
            mask_path=args.mask,
            prompt=args.prompt,
            num_steps=args.steps,
            guidance_scale=args.guidance,
            auto_mask_threshold=args.threshold,
            debug=args.debug
        )
        return 0
    except Exception as e:
        print(f"Error during restoration: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
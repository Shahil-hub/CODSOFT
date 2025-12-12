"""
CLEAN IMAGE CAPTIONING - NO WARNINGS VERSION
=============================================
This version shows only the results, no warnings or extra messages!
"""

# Suppress all warnings and messages
import warnings
warnings.filterwarnings('ignore')

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'

# Import libraries (silently)
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from transformers import logging as transformers_logging
transformers_logging.set_verbosity_error()

import torch
from PIL import Image

# Load model silently
print("Loading model...")
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
print("Model ready!\n")

def caption_image(image_path):
    """Generate caption for an image (silent mode)"""
    image = Image.open(image_path)
    if image.mode != "RGB":
        image = image.convert(mode="RGB")
    
    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)
    
    # Generate with no warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        output_ids = model.generate(pixel_values, max_length=16, num_beams=4)
    
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return caption

# ========== CHANGE YOUR IMAGE HERE ==========
image_path = "Sunset.jpg"  # 👈 Change to your image!
# ============================================

print("="*50)
print("IMAGE CAPTIONING RESULTS")
print("="*50 + "\n")

# Caption single image
if os.path.exists(image_path):
    caption = caption_image(image_path)
    print(f"📸 {image_path}")
    print(f"💬 {caption}\n")
else:
    print(f"❌ File not found: {image_path}\n")

# Caption multiple images
print("-"*50)
print("Multiple Images:")
print("-"*50 + "\n")

# ========== ADD YOUR IMAGES HERE ==========
images = [
    "cat.jpg",
    "dog.jpg"
]
# ==========================================

for img in images:
    if os.path.exists(img):
        caption = caption_image(img)
        print(f"📸 {img} → {caption}")
    else:
        print(f"⚠️  {img} → Not found")

print("\n" + "="*50)
print("✅ Done!")
print("="*50)
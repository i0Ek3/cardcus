from PIL import Image
import os
import re

def convert_to_card(input_image_path):
    # Get base filename without extension
    base_name = os.path.splitext(os.path.basename(input_image_path))[0]
    output_name = f"card_{base_name}.jpg"

    # Open image
    try:
        img = Image.open(input_image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return False

    # Get image DPI info
    try:
        dpi_x, dpi_y = img.info['dpi']
    except:
        # If no DPI info, calculate from pixel dimensions
        # Standard card size in mm converted to inches
        width_in = 88.5 / 25.4  # Convert mm to inches
        height_in = 57.5 / 25.4

        # Calculate effective DPI
        dpi_x = img.width / width_in
        dpi_y = img.height / height_in

    # Check if resolution is too low
    if min(dpi_x, dpi_y) < 350:
        print("Image resolution too low. Please provide an image with at least 350 DPI")
        return False

    # Calculate target size in pixels for 88.5mm x 57.5mm at image's DPI
    target_width = int(88.5 / 25.4 * dpi_x)  # Convert mm to inches then to pixels
    target_height = int(57.5 / 25.4 * dpi_y)

    # Resize image maintaining aspect ratio
    img_ratio = img.width / img.height
    target_ratio = target_width / target_height

    if img_ratio > target_ratio:
        # Image is wider than target
        new_width = target_width
        new_height = int(target_width / img_ratio)
    else:
        # Image is taller than target
        new_height = target_height
        new_width = int(target_height * img_ratio)

    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Create blank white canvas of target size
    final_img = Image.new('RGB', (target_width, target_height), 'white')

    # Paste resized image centered on canvas
    paste_x = (target_width - new_width) // 2
    paste_y = (target_height - new_height) // 2
    final_img.paste(img, (paste_x, paste_y))

    # Save as JPEG
    try:
        final_img.save(output_name, 'JPEG', quality=95, dpi=(dpi_x, dpi_y))
        print(f"Successfully converted image to card format: {output_name}")
        return True
    except Exception as e:
        print(f"Error saving image: {e}")
        return False

# Example usage
if __name__ == "__main__":
    input_path = input("Please enter the path to your image: ")
    convert_to_card(input_path)

import json
import os

from pdf2image import convert_from_path
import pytesseract

# Path to the Tesseract OCR executable (update this if needed)
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update for Windows
# For Linux or Mac, you might not need this line if tesseract is in your PATH

def pdf_to_images(pdf_path):
    """Convert PDF pages to images."""
    images = convert_from_path(pdf_path)
    return images

def extract_text_from_image(image):
    """Use OCR to extract text from the given image."""
    return pytesseract.image_to_string(image)

def pdf_to_json(pdf_path, output_json_path):
    """Convert PDF to JSON with text blobs."""
    images = pdf_to_images(pdf_path)
    text_blobs = {}

    for i, image in enumerate(images):
        text = extract_text_from_image(image)
        text_blobs[f'blob_{i + 1}'] = text.strip()

    with open(output_json_path, 'w') as json_file:
        json.dump(text_blobs, json_file, indent=4)

    print(f"Extracted text blobs saved to {output_json_path}")


if __name__ == "__main__":
    input_pdf = "Erste_5-DE.pdf"
    output_json = 'output.json'

    pdf_to_json(input_pdf, output_json)

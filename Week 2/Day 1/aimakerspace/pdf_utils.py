# pip install PyMuPDF Pillow pytesseract

import os 
from PyPDF2 import PdfReader
import logging

"""
import fitz  # PyMuPDF
import io
from PIL import Image
import pytesseract
"""

class PdfFileLoader:
    def __init__(self, path: str):
        self.documents = []
        self.path = path

        # Configure logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)  # Set logging level to DEBUG
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # Configure console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)  # Set console logging level to DEBUG
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def load(self):
        self.logger.info("Provided path: %s", self.path)
        if os.path.isfile(self.path) and self.path.endswith(".pdf"):
            self.load_pdf()
        else:
            raise ValueError("Provided path is not a valid PDF file.")

    def load_pdf(self):
        try:
            with open(self.path, "rb") as file:
                pdf_reader = PdfReader(file)
                num_pages = len(pdf_reader.pages)
                all_text = ""
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    self.logger.info("Processing page %d/%d", page_num + 1, num_pages)
                    all_text += page.extract_text()
                self.documents.append(all_text)
        except Exception as e:
            self.logger.error("Failed to open or extract text from PDF file: %s", e)

    def load_documents(self):
        self.logger.info("Running load().")
        self.load()
        return self.documents


if __name__ == "__main__":
    loader = PdfFileLoader("/home/bokhard/AIMS/AIE2-class/Week 2/Day 1/aimakerspace/KingLear.pdf")
    loader.load()
    if loader.documents:
        print(loader.documents[0])
    else:
        print("No text extracted from the PDF.")



""" 
    def load_pdf(self):
        try:
            doc = fitz.open(self.path)
        except Exception as e:
            print(f"Failed to open PDF file: {e}")
            return

        all_text = ""

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            print(f"Processing page {page_num + 1}/{len(doc)}")
            
            images = page.get_images(full=True)
            print(f"Number of images found on page {page_num + 1}: {len(images)}")

            for img_index, img in enumerate(page.get_images(full=True)):
                print(f"Extracting image {img_index + 1} on page {page_num + 1}")
                base_image = doc.extract_image(img[0])
                image_bytes = base_image["image"]
                image = Image.open(io.BytesIO(image_bytes))

                # Debugging Tesseract OCR
                print("Performing OCR on the extracted image...")
                text = pytesseract.image_to_string(image, lang='eng')
                print("Extracted text:", text)

                all_text += text

        self.documents.append(all_text) 
"""
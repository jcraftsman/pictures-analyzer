from PIL import Image
from pytesseract import image_to_string

from pictures_analyzer.domain.file import File
from pictures_analyzer.domain.ocr import OCR


class TesseractOCR(OCR):

    def image_to_text(self, file: File) -> str:
        return image_to_string(Image.open(file.path))

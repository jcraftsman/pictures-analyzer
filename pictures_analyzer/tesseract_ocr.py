from PIL import Image
from pytesseract import image_to_string

from pictures_analyzer.file import File
from pictures_analyzer.invalid_file_exception import InvalidFileException
from pictures_analyzer.ocr import OCR


class TesseractOCR(OCR):

    def image_to_text(self, file: File) -> str:
        try:
            return image_to_string(Image.open(file.path))
        except Exception:
            raise InvalidFileException()


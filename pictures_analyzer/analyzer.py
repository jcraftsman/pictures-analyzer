from pictures_analyzer.finder import Finder
from pictures_analyzer.ocr import OCR
from pictures_analyzer.safe_box import SafeBox
from pictures_analyzer.search_engine import SearchEngine


class Analyzer(object):

    def __init__(self, search_engine: SearchEngine, safe_box: SafeBox, finder: Finder, ocr: OCR):
        self.ocr = ocr
        self.finder = finder
        self.safe_box = safe_box
        self.search_engine = search_engine

    def index(self, pictures_directory_path) -> None:
        files = self.finder.list_directory(pictures_directory_path)
        for file in files:
            url = self.safe_box.upload(file.path)
            ocr_image_to_text = self.ocr.image_to_text(file)
            self.search_engine.index({'name': file.name,
                                      'url': url,
                                      'description': ocr_image_to_text})

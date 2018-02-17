from pictures_analyzer.safe_box import SafeBox
from pictures_analyzer.search_engine import SearchEngine


class Analyzer(object):

    def __init__(self, search_engine: SearchEngine, safe_box: SafeBox, finder):
        self.finder = finder
        self.safe_box = safe_box
        self.search_engine = search_engine

    def index(self, pictures_directory_path):
        files = self.finder.list_directory(pictures_directory_path)
        for file in files:
            url = self.safe_box.upload(file)
            self.search_engine.index({'name': '',
                                      'url': url,
                                      'description': ''})

from typing import List

from pictures_analyzer.file import File


class Finder(object):
    def list_directory(self, directory_path) -> List[File]:
        raise NotImplementedError()

import os
from os import path
from typing import List

from pictures_analyzer.file import File
from pictures_analyzer.finder import Finder


class LocalFilesFinder(Finder):
    def list_directory(self, directory_path) -> List[File]:
        files_in_directory = list()
        file_names_in_directory = os.listdir(directory_path)
        for file_name in file_names_in_directory:
            file_path = path.join(directory_path, file_name)
            file = File(name=file_name, path=file_path)
            files_in_directory.append(file)
        return files_in_directory

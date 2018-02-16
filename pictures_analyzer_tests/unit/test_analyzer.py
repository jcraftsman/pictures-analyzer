from unittest import TestCase
from unittest.mock import Mock, call

from pictures_analyzer.analyzer import Analyzer


class TestAnalyzer(TestCase):

    def setUp(self):
        self.search_engine = Mock()
        self.safe_box = Mock()
        self.finder = Mock()
        self.analyzer = Analyzer(self.search_engine, self.safe_box, self.finder)

    def test_index_should_upload_a_file_to_safebox_when_there_is_one_file_in_directory(self):
        # Given
        picture_path = './top_secrets.png'
        self.finder.list_directory.return_value = [picture_path]

        # When
        self.analyzer.index('./pictures')

        # Then
        self.safe_box.upload.assert_called_once_with(picture_path)
        self.finder.list_directory.assert_called_once_with('./pictures')

    def test_index_should_upload_files_to_safebox_when_there_is_three_files_in_directory(self):
        # Given
        picture_path_1 = './top_secrets_1.png'
        picture_path_2 = './top_secrets_2.png'
        picture_path_3 = './top_secrets_3.png'
        self.finder.list_directory.return_value = [picture_path_1, picture_path_2, picture_path_3]

        # When
        self.analyzer.index('./pictures')

        # Then
        self.safe_box.upload.has_calls([
            call(picture_path_1),
            call(picture_path_2),
            call(picture_path_3)
        ])
        self.finder.list_directory.assert_called_once_with('./pictures')


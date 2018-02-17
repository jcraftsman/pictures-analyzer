from unittest import TestCase
from unittest.mock import Mock, call, ANY

from file import File
from pictures_analyzer.analyzer import Analyzer

PUBLISHED_PICTURE_URL = 'https://s3.eu-west-3.amazonaws.com/evolutionary-confidential/agent-phillip/top_secret.png'

IMAGE_TO_TEXT = 'Rezidentura'


class TestAnalyzer(TestCase):

    def setUp(self):
        self.search_engine = Mock()
        self.safe_box = Mock()
        self.finder = Mock()
        self.optical_character_recognition = Mock()
        self.analyzer = Analyzer(self.search_engine, self.safe_box, self.finder, self.optical_character_recognition)

    def test_index_should_upload_a_file_to_safebox_when_there_is_one_file_in_directory(self):
        # Given
        picture_path = './top_secrets.png'
        self.finder.list_directory.return_value = [File(path=picture_path)]

        # When
        self.analyzer.index('./pictures')

        # Then
        self.safe_box.upload.assert_called_once_with(picture_path)
        self.finder.list_directory.assert_called_once_with('./pictures')

    def test_index_should_upload_files_to_safebox_when_there_is_three_files_in_directory(self):
        # Given
        picture_file_1 = File(path='./top_secrets_1.png')
        picture_file_2 = File(path='./top_secrets_2.png')
        picture_file_3 = File(path='./top_secrets_3.png')
        self.finder.list_directory.return_value = [picture_file_1, picture_file_2, picture_file_3]

        # When
        self.analyzer.index('./pictures')

        # Then
        self.safe_box.upload.has_calls([
            call(picture_file_1),
            call(picture_file_2),
            call(picture_file_3)
        ])
        self.finder.list_directory.assert_called_once_with('./pictures')

    def test_index_should_send_the_uploaded_url_to_the_search_engine_when_one_file_is_uploaded(self):
        # Given
        picture = File(path='./top_secrets.png')
        self.finder.list_directory.return_value = [picture]
        self.safe_box.upload.side_effect = [PUBLISHED_PICTURE_URL]

        # When
        self.analyzer.index('./pictures')

        # Then
        self.search_engine.index.assert_called_once_with({'name': ANY,
                                                          'url': PUBLISHED_PICTURE_URL,
                                                          'description': ANY})

    def test_index_should_send_all_the_uploaded_urls_to_the_search_engine_when_three_files_are_uploaded(self):
        # Given
        picture_file = File(path='./top_secrets.png')
        self.finder.list_directory.return_value = [picture_file, picture_file, picture_file]
        uploaded_picture_1 = 'https://url1'
        uploaded_picture_2 = 'https://url2'
        uploaded_picture_3 = 'https://url3'
        self.safe_box.upload.side_effect = [uploaded_picture_1, uploaded_picture_2, uploaded_picture_3]

        # When
        self.analyzer.index('./pictures')

        # Then
        self.search_engine.index.assert_has_calls([
            call({'name': ANY, 'url': uploaded_picture_1, 'description': ANY}),
            call({'name': ANY, 'url': uploaded_picture_2, 'description': ANY}),
            call({'name': ANY, 'url': uploaded_picture_3, 'description': ANY})
        ])

    def test_index_should_fill_the_picture_name_in_the_payload_sent_to_search_engine_indexer(self):
        # Given
        picture_file = File(path='./top_secrets.png', name='top_secrets.png')
        self.finder.list_directory.return_value = [picture_file]

        # When
        self.analyzer.index('./pictures')

        # Then
        self.search_engine.index.assert_called_once_with({'name': 'top_secrets.png',
                                                          'url': ANY,
                                                          'description': ANY})

    def test_index_should_fill_the_description_with_ocr_picture_to_textn_in_the_payload_sent_to_search_engine(self):
        # Given
        picture_file = File()
        self.finder.list_directory.return_value = [picture_file]
        self.optical_character_recognition.image_to_text.return_value = IMAGE_TO_TEXT

        # When
        self.analyzer.index('./pictures')

        # Then
        self.search_engine.index.assert_called_once_with({'name': ANY,
                                                          'url': ANY,
                                                          'description': IMAGE_TO_TEXT})
        self.optical_character_recognition.image_to_text.assert_called_once_with(picture_file)

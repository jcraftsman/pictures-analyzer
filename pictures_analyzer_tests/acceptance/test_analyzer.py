import os
from unittest import TestCase
from unittest.mock import Mock

from pictures_analyzer.analyzer import Analyzer

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

PICTURES_DIRECTORY_PATH = CURRENT_PATH + '/pictures'

PUBLISHED_PICTURE_URL = 'https://s3.eu-west-3.amazonaws.com/evolutionary-confidential/agent-phillip/top_secret.png'

IMAGE_TO_TEXT = 'Rezidentura'


class TestAnalyzer(TestCase):

    def setUp(self):
        self.search_engine = Mock()
        self.safe_box = Mock()
        self.analyzer = Analyzer(self.search_engine, self.safe_box, self.finder)

    def test_index_should_use_search_engine_to_index_published_image_and_the_text_it_contains(self):
        # Given
        self.safe_box.upload.side_effect = [PUBLISHED_PICTURE_URL]

        # When
        self.analyzer.index(PICTURES_DIRECTORY_PATH)

        # Then
        self.search_engine.index.assert_called_once_with({'name': 'top_secret.png',
                                                          'url': PUBLISHED_PICTURE_URL,
                                                          'description': IMAGE_TO_TEXT})
        self.safe_box.upload.assert_called_once_with(PICTURES_DIRECTORY_PATH + '/top_secret.png')

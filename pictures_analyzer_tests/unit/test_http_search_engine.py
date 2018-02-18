from unittest import TestCase
from unittest.mock import Mock, patch

import requests_mock

from pictures_analyzer.http_search_engine import HttpSearchEngine

SEARCH_ENGINE_URL = 'https://search-engine.secure.api.wal'

PICTURE_ANALYSIS_PAYLOAD = {'name': 'picture.jpg',
                            'url': 'https://bucket/agent-folder/picture.jpg',
                            'description': 'The text in the picture'}


class TestSearchEngine(TestCase):

    def setUp(self):
        self.environment = Mock()
        self.http_search_engine = HttpSearchEngine(self.environment)

    @patch('requests.post')
    def test_index_should_post_picture_analysis_payload_using_url_in_environment(self, requests_post_mock):
        # Given
        self.environment.get.return_value = SEARCH_ENGINE_URL

        # When
        self.http_search_engine.index(PICTURE_ANALYSIS_PAYLOAD)

        # Then
        requests_post_mock.assert_called_once_with(url=SEARCH_ENGINE_URL, json=PICTURE_ANALYSIS_PAYLOAD)
        self.environment.get.assert_called_once_with('SEARCH_ENGINE_URL')

    def test_index_should_return_the_response_json_when_the_post_succeeds(self):
        # Given
        self.environment.get.return_value = SEARCH_ENGINE_URL
        successful_indexing_response = {'_id': '007'}
        with requests_mock.mock() as mock:
            mock.post(url=SEARCH_ENGINE_URL, json=successful_indexing_response)

            # When
            response = self.http_search_engine.index(PICTURE_ANALYSIS_PAYLOAD)

            # Then
            self.assertEqual(response, successful_indexing_response)

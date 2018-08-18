import requests

from pictures_analyzer.domain.search_engine import SearchEngine


class HttpSearchEngine(SearchEngine):

    def __init__(self, environment):
        self.environment = environment

    def index(self, picture_analysis: dict) -> dict:
        search_engine_url = self.environment.get('SEARCH_ENGINE_URL')
        search_engine_http_response = requests.post(url=search_engine_url, json=picture_analysis)
        return search_engine_http_response.json()

from django.test import TestCase
from .utils import requests


class CoreTestCase(TestCase):
    def test_coins(self):
        data = requests.get_coins(5, 1, 'market_cap', False)
        assert len(data) > 0

    def test_overview(self):
        data = requests.get_overview()
        assert len(data) > 0

    def test_search(self):
        data = requests.search_coins('bit')
        assert len(data) > 0

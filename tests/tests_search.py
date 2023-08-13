import unittest
from unittest.mock import Mock, patch
from jetphotos.search import Search


class TestSearch(unittest.TestCase):
    @patch("jetphotos.search.requests.get")
    def test_aircraft(self, mock_get):
        mock_response = Mock()
        mock_response.content = b'<html><div class="result__section result__section--photo-wrapper"><img src="//example.com/photo.jpg"></div></html>'
        mock_get.return_value = mock_response

        expected_url = "https://example.com/photo.jpg"
        result_url = Search.aircraft(prefix="PT-RVT")

        self.assertEqual(result_url, expected_url)

import unittest
from unittest.mock import patch
from jetphotos.search import Search


class TestSearch(unittest.TestCase):
    @patch("jetphotos.search.requests.get")
    def test_aircraft(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.content = b"<html>"
        mock_response.content += b'<div class="result__section result__section--photo-wrapper">'
        mock_response.content += b'<img src="//example.com/photo.jpg">'
        mock_response.content += b"</div>"
        mock_response.content += b"</html>"

        result_url = Search.aircraft(prefix="PT-RVT")

        expected_url = "https://example.com/photo.jpg"

        self.assertEqual(result_url, expected_url)

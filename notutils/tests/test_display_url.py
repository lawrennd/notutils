"""
Unit tests for display_url function.
"""
import pytest
from unittest.mock import patch, MagicMock
from notutils import display_url


class TestDisplayUrl:
    """Test cases for display_url function."""

    @patch('notutils.notutils.display')
    def test_display_url_with_http_prefix(self, mock_display):
        url = "https://www.example.com"
        display_url(url)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        # call_args is an HTML object, so we need to check its data attribute
        html_str = call_args.data
        assert url in html_str
        assert 'target=_blank' in html_str

    @patch('notutils.notutils.display')
    def test_display_url_without_http_prefix(self, mock_display):
        url = "www.example.com"
        display_url(url)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_str = call_args.data
        assert "http://www.example.com" in html_str
        assert 'target=_blank' in html_str

    @patch('notutils.notutils.display')
    def test_display_url_with_https_prefix(self, mock_display):
        url = "https://www.example.com"
        display_url(url)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_str = call_args.data
        assert url in html_str
        assert 'target=_blank' in html_str

    @patch('notutils.notutils.display')
    def test_display_url_empty_string(self, mock_display):
        url = ""
        display_url(url)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_str = call_args.data
        assert "http://" in html_str

    @patch('notutils.notutils.display')
    def test_display_url_special_characters(self, mock_display):
        url = "https://example.com/path?param=value&other=123"
        display_url(url)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_str = call_args.data
        assert url in html_str
        assert 'target=_blank' in html_str

    @patch('notutils.notutils.display')
    def test_display_url_unicode(self, mock_display):
        url = "https://example.com/unicode/测试"
        display_url(url)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_str = call_args.data
        assert url in html_str
        assert 'target=_blank' in html_str 
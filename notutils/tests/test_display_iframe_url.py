"""
Unit tests for display_iframe_url function.
"""
import pytest
from unittest.mock import patch, MagicMock
from notutils import display_iframe_url, iframe_url


class TestDisplayIframeUrl:
    """Test cases for display_iframe_url function."""

    @patch('notutils.notutils.display')
    def test_display_iframe_url_basic(self, mock_display):
        url = "https://www.example.com"
        display_iframe_url(url)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_str = call_args.data
        assert "iframe" in html_str
        assert url in html_str

    @patch('notutils.notutils.display')
    def test_display_iframe_url_with_kwargs(self, mock_display):
        url = "https://www.example.com"
        display_iframe_url(url, width=800, height=600, scrolling=False)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_str = call_args.data
        assert 'width=800' in html_str
        assert 'height=600' in html_str
        assert 'scrolling="no"' in html_str

    @patch('notutils.notutils.display')
    def test_display_iframe_url_without_http_prefix(self, mock_display):
        url = "www.example.com"
        display_iframe_url(url)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_str = call_args.data
        assert "http://www.example.com" in html_str

    @patch('notutils.notutils.display')
    def test_display_iframe_url_all_parameters(self, mock_display):
        url = "https://www.example.com"
        display_iframe_url(
            url, 
            width=1000, 
            height=800, 
            scrolling=False, 
            border=10, 
            frameborder=5
        )
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_str = call_args.data
        assert 'width=1000' in html_str
        assert 'height=800' in html_str
        assert 'scrolling="no"' in html_str
        assert 'border:10px' in html_str
        assert 'frameborder="5"' in html_str

    @patch('notutils.notutils.display')
    def test_display_iframe_url_empty_string(self, mock_display):
        url = ""
        display_iframe_url(url)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_str = call_args.data
        assert "http://" in html_str
        assert "iframe" in html_str

    @patch('notutils.notutils.display')
    def test_display_iframe_url_special_characters(self, mock_display):
        url = "https://example.com/path?param=value&other=123"
        display_iframe_url(url)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_str = call_args.data
        assert url in html_str
        assert "iframe" in html_str

    @patch('notutils.notutils.display')
    def test_display_iframe_url_unicode(self, mock_display):
        url = "https://example.com/unicode/测试"
        display_iframe_url(url)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_str = call_args.data
        assert url in html_str
        assert "iframe" in html_str

    def test_display_iframe_url_uses_iframe_url(self):
        url = "https://www.example.com"
        expected_html = iframe_url(url, width=800, height=600)
        with patch('notutils.notutils.display') as mock_display:
            display_iframe_url(url, width=800, height=600)
            actual_html = mock_display.call_args[0][0].data
            assert "iframe" in actual_html
            assert url in actual_html
            assert 'width=800' in actual_html
            assert 'height=600' in actual_html 
"""
Unit tests for iframe_url function.
"""
import pytest
from notutils import iframe_url


class TestIframeUrl:
    """Test cases for iframe_url function."""

    def test_iframe_url_basic(self):
        """Test iframe_url with basic parameters."""
        url = "https://www.example.com"
        result = iframe_url(url)
        
        assert "iframe" in result
        assert url in result
        assert 'width=500' in result
        assert 'height=400' in result
        assert 'scrolling="yes"' in result
        assert 'frameborder="0"' in result

    def test_iframe_url_without_http_prefix(self):
        """Test iframe_url with URL that doesn't have http prefix."""
        url = "www.example.com"
        result = iframe_url(url)
        
        assert "http://www.example.com" in result
        assert 'width=500' in result
        assert 'height=400' in result

    def test_iframe_url_custom_dimensions(self):
        """Test iframe_url with custom width and height."""
        url = "https://www.example.com"
        result = iframe_url(url, width=800, height=600)
        
        assert 'width=800' in result
        assert 'height=600' in result

    def test_iframe_url_no_scrolling(self):
        """Test iframe_url with scrolling disabled."""
        url = "https://www.example.com"
        result = iframe_url(url, scrolling=False)
        
        assert 'scrolling="no"' in result

    def test_iframe_url_custom_border(self):
        """Test iframe_url with custom border."""
        url = "https://www.example.com"
        result = iframe_url(url, border=5)
        
        assert 'border:5px' in result

    def test_iframe_url_custom_frameborder(self):
        """Test iframe_url with custom frameborder."""
        url = "https://www.example.com"
        result = iframe_url(url, frameborder=1)
        
        assert 'frameborder="1"' in result

    def test_iframe_url_all_custom_parameters(self):
        """Test iframe_url with all custom parameters."""
        url = "https://www.example.com"
        result = iframe_url(
            url, 
            width=1000, 
            height=800, 
            scrolling=False, 
            border=10, 
            frameborder=5
        )
        
        assert 'width=1000' in result
        assert 'height=800' in result
        assert 'scrolling="no"' in result
        assert 'border:10px' in result
        assert 'frameborder="5"' in result

    def test_iframe_url_empty_string(self):
        """Test iframe_url with empty string."""
        url = ""
        result = iframe_url(url)
        
        assert "http://" in result
        assert "iframe" in result

    def test_iframe_url_special_characters(self):
        """Test iframe_url with URL containing special characters."""
        url = "https://example.com/path?param=value&other=123"
        result = iframe_url(url)
        
        assert url in result
        assert "iframe" in result

    def test_iframe_url_unicode(self):
        """Test iframe_url with unicode URL."""
        url = "https://example.com/unicode/测试"
        result = iframe_url(url)
        
        assert url in result
        assert "iframe" in result 
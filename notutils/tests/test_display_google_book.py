"""
Unit tests for display_google_book function.
"""
import pytest
from unittest.mock import patch, MagicMock
from notutils import display_google_book


class TestDisplayGoogleBook:
    """Test cases for display_google_book function."""

    @patch('notutils.notutils.IFrame')
    def test_display_google_book_basic(self, mock_iframe):
        book_id = "test123"
        display_google_book(book_id)
        mock_iframe.assert_called_once()
        call_args = mock_iframe.call_args
        url = call_args.args[0]
        kwargs = call_args.kwargs
        assert "books.google.co.uk/books" in url
        assert f"id={book_id}" in url
        assert "output=embed" in url
        assert kwargs['width'] == 600
        assert kwargs['height'] == 450

    @patch('notutils.notutils.IFrame')
    def test_display_google_book_with_int_page(self, mock_iframe):
        book_id = "test123"
        page = 42
        display_google_book(book_id, page=page)
        mock_iframe.assert_called_once()
        call_args = mock_iframe.call_args
        url = call_args.args[0]
        kwargs = call_args.kwargs
        assert f"pg=PA{page}" in url
        assert f"id={book_id}" in url

    @patch('notutils.notutils.IFrame')
    def test_display_google_book_with_string_page(self, mock_iframe):
        book_id = "test123"
        page = "PR5"
        display_google_book(book_id, page=page)
        mock_iframe.assert_called_once()
        call_args = mock_iframe.call_args
        url = call_args.args[0]
        kwargs = call_args.kwargs
        assert f"pg={page}" in url
        assert f"id={book_id}" in url

    @patch('notutils.notutils.IFrame')
    def test_display_google_book_custom_dimensions(self, mock_iframe):
        book_id = "test123"
        display_google_book(book_id, width=800, height=600)
        mock_iframe.assert_called_once()
        call_args = mock_iframe.call_args
        url = call_args.args[0]
        kwargs = call_args.kwargs
        assert kwargs['width'] == 800
        assert kwargs['height'] == 600

    @patch('notutils.notutils.IFrame')
    def test_display_google_book_with_kwargs(self, mock_iframe):
        book_id = "test123"
        display_google_book(book_id, width=800, height=600, frameborder=1)
        mock_iframe.assert_called_once()
        call_args = mock_iframe.call_args
        url = call_args.args[0]
        kwargs = call_args.kwargs
        assert kwargs['width'] == 800
        assert kwargs['height'] == 600
        assert kwargs['frameborder'] == 1

    @patch('notutils.notutils.IFrame')
    def test_display_google_book_page_zero(self, mock_iframe):
        book_id = "test123"
        page = 0
        display_google_book(book_id, page=page)
        mock_iframe.assert_called_once()
        call_args = mock_iframe.call_args
        url = call_args.args[0]
        kwargs = call_args.kwargs
        assert "pg=PA0" in url

    @patch('notutils.notutils.IFrame')
    def test_display_google_book_negative_page(self, mock_iframe):
        book_id = "test123"
        page = -5
        display_google_book(book_id, page=page)
        mock_iframe.assert_called_once()
        call_args = mock_iframe.call_args
        url = call_args.args[0]
        kwargs = call_args.kwargs
        assert "pg=PA-5" in url

    @patch('notutils.notutils.IFrame')
    def test_display_google_book_special_characters_in_id(self, mock_iframe):
        book_id = "test_123-456"
        display_google_book(book_id)
        mock_iframe.assert_called_once()
        call_args = mock_iframe.call_args
        url = call_args.args[0]
        kwargs = call_args.kwargs
        assert f"id={book_id}" in url

    @patch('notutils.notutils.IFrame')
    def test_display_google_book_unicode_id(self, mock_iframe):
        book_id = "test_测试_123"
        display_google_book(book_id)
        mock_iframe.assert_called_once()
        call_args = mock_iframe.call_args
        url = call_args.args[0]
        kwargs = call_args.kwargs
        assert f"id={book_id}" in url 
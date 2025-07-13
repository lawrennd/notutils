"""
Unit tests for code_toggle function.
"""
import pytest
from unittest.mock import patch, MagicMock
from notutils import code_toggle


class TestCodeToggle:
    """Test cases for code_toggle function."""

    @patch('notutils.notutils.display')
    def test_code_toggle_default_parameters(self, mock_display):
        code_toggle()
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_content = call_args.data
        assert "The raw code for this jupyter notebook can be hidden for easier reading" in html_content
        assert "code_show=false" in html_content
        assert "javascript:code_toggle()" in html_content
        assert "<script>" in html_content

    @patch('notutils.notutils.display')
    def test_code_toggle_start_show_true(self, mock_display):
        code_toggle(start_show=True)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_content = call_args.data
        assert "code_show=true" in html_content

    @patch('notutils.notutils.display')
    def test_code_toggle_custom_message(self, mock_display):
        custom_message = "Custom toggle message"
        code_toggle(message=custom_message)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_content = call_args.data
        assert custom_message in html_content

    @patch('notutils.notutils.display')
    def test_code_toggle_start_show_true_custom_message(self, mock_display):
        custom_message = "Show/hide code cells"
        code_toggle(start_show=True, message=custom_message)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_content = call_args.data
        assert "code_show=true" in html_content
        assert custom_message in html_content

    @patch('notutils.notutils.display')
    def test_code_toggle_html_structure(self, mock_display):
        code_toggle()
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_content = call_args.data
        assert "<script>" in html_content
        assert "</script>" in html_content
        assert "function code_toggle()" in html_content
        assert "$('div.input').show()" in html_content
        assert "$('div.input').hide()" in html_content
        assert "code_show = !code_show" in html_content
        assert "$( document ).ready(code_toggle)" in html_content

    @patch('notutils.notutils.display')
    def test_code_toggle_javascript_functionality(self, mock_display):
        code_toggle()
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_content = call_args.data
        assert "if (code_show)" in html_content
        assert "else" in html_content
        assert "code_show = !code_show" in html_content

    @patch('notutils.notutils.display')
    def test_code_toggle_link_generation(self, mock_display):
        code_toggle()
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_content = call_args.data
        assert 'href="javascript:code_toggle()"' in html_content
        assert "click" in html_content

    @patch('notutils.notutils.display')
    def test_code_toggle_empty_message(self, mock_display):
        code_toggle(message="")
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_content = call_args.data
        assert 'href="javascript:code_toggle()"' in html_content

    @patch('notutils.notutils.display')
    def test_code_toggle_special_characters_in_message(self, mock_display):
        message_with_special = "Toggle code with 'quotes' and \"double quotes\""
        code_toggle(message=message_with_special)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_content = call_args.data
        assert message_with_special in html_content

    @patch('notutils.notutils.display')
    def test_code_toggle_unicode_message(self, mock_display):
        unicode_message = "切换代码显示 测试"
        code_toggle(message=unicode_message)
        mock_display.assert_called_once()
        call_args = mock_display.call_args[0][0]
        html_content = call_args.data
        assert unicode_message in html_content 
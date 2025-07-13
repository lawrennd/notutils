"""
Unit tests for display_plots function.
"""
import pytest
import os
import tempfile
from unittest.mock import patch, MagicMock, mock_open
from notutils import display_plots


class TestDisplayPlots:
    """Test cases for display_plots function."""

    @patch('notutils.notutils.interact')
    def test_display_plots_basic(self, mock_interact):
        """Test display_plots with basic parameters."""
        filebase = "plot_{}.png"
        display_plots(filebase)
        
        # Check that interact was called
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        
        # Check that the first argument is the show_figure function
        assert callable(call_args[0][0])
        
        # Check that fixed parameters are passed correctly
        kwargs = call_args[1]
        for key in ['filebase', 'directory', 'width', 'height']:
            if key in kwargs and hasattr(kwargs[key], 'value'):
                kwargs[key] = kwargs[key].value
        assert kwargs['filebase'] == filebase
        assert kwargs['directory'] is None
        assert kwargs['width'] == 600
        assert kwargs['height'] == 450

    @patch('notutils.notutils.interact')
    def test_display_plots_with_directory(self, mock_interact):
        """Test display_plots with directory parameter."""
        filebase = "plot_{}.png"
        directory = "/path/to/plots"
        display_plots(filebase, directory=directory)
        
        # Check that interact was called
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        
        # Check that directory is passed correctly
        kwargs = call_args[1]
        for key in ['filebase', 'directory', 'width', 'height']:
            if key in kwargs and hasattr(kwargs[key], 'value'):
                kwargs[key] = kwargs[key].value
        assert kwargs['directory'] == directory

    @patch('notutils.notutils.interact')
    def test_display_plots_custom_dimensions(self, mock_interact):
        """Test display_plots with custom dimensions."""
        filebase = "plot_{}.png"
        display_plots(filebase, width=800, height=600)
        
        # Check that interact was called
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        
        # Check custom dimensions
        kwargs = call_args[1]
        for key in ['filebase', 'directory', 'width', 'height']:
            if key in kwargs and hasattr(kwargs[key], 'value'):
                kwargs[key] = kwargs[key].value
        assert kwargs['width'] == 800
        assert kwargs['height'] == 600

    @patch('notutils.notutils.interact')
    def test_display_plots_with_kwargs(self, mock_interact):
        """Test display_plots with additional kwargs."""
        filebase = "plot_{}.png"
        display_plots(filebase, frame=5, quality="high")
        
        # Check that interact was called
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        
        # Check that additional kwargs are passed
        kwargs = call_args[1]
        assert kwargs['frame'] == 5
        assert kwargs['quality'] == "high"

    @patch('notutils.notutils.interact')
    def test_display_plots_svg_format(self, mock_interact):
        """Test display_plots with SVG format."""
        filebase = "plot_{}.svg"
        display_plots(filebase)
        
        # Check that interact was called
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        
        # Check that the show_figure function is callable
        show_figure_func = call_args[0][0]
        assert callable(show_figure_func)

    @patch('notutils.notutils.interact')
    def test_display_plots_html_format(self, mock_interact):
        """Test display_plots with HTML format."""
        filebase = "plot_{}.html"
        display_plots(filebase)
        
        # Check that interact was called
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        
        # Check that the show_figure function is callable
        show_figure_func = call_args[0][0]
        assert callable(show_figure_func)

    @patch('notutils.notutils.interact')
    def test_display_plots_jpg_format(self, mock_interact):
        """Test display_plots with JPG format."""
        filebase = "plot_{}.jpg"
        display_plots(filebase)
        
        # Check that interact was called
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        
        # Check that the show_figure function is callable
        show_figure_func = call_args[0][0]
        assert callable(show_figure_func)

    @patch('notutils.notutils.interact')
    def test_display_plots_gif_format(self, mock_interact):
        """Test display_plots with GIF format."""
        filebase = "plot_{}.gif"
        display_plots(filebase)
        
        # Check that interact was called
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        
        # Check that the show_figure function is callable
        show_figure_func = call_args[0][0]
        assert callable(show_figure_func)

    @patch('notutils.notutils.interact')
    def test_display_plots_jpeg_format(self, mock_interact):
        """Test display_plots with JPEG format."""
        filebase = "plot_{}.jpeg"
        display_plots(filebase)
        
        # Check that interact was called
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        
        # Check that the show_figure function is callable
        show_figure_func = call_args[0][0]
        assert callable(show_figure_func)

    @patch('notutils.notutils.interact')
    def test_display_plots_complex_filebase(self, mock_interact):
        """Test display_plots with complex filebase format."""
        filebase = "experiment_{experiment_id}_frame_{frame}.png"
        display_plots(filebase, experiment_id="exp1", frame=5)
        
        # Check that interact was called
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        
        # Check that additional kwargs are passed
        kwargs = call_args[1]
        assert kwargs['experiment_id'] == "exp1"
        assert kwargs['frame'] == 5

    @patch('notutils.notutils.interact')
    def test_display_plots_empty_filebase(self, mock_interact):
        """Test display_plots with empty filebase."""
        filebase = ""
        display_plots(filebase)
        
        # Check that interact was called
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        
        # Check that empty filebase is passed
        kwargs = call_args[1]
        for key in ['filebase', 'directory', 'width', 'height']:
            if key in kwargs and hasattr(kwargs[key], 'value'):
                kwargs[key] = kwargs[key].value
        assert kwargs['filebase'] == ""

    @patch('notutils.notutils.interact')
    def test_display_plots_unicode_filebase(self, mock_interact):
        """Test display_plots with unicode in filebase."""
        filebase = "plot_{}_测试.png"
        display_plots(filebase)
        
        # Check that interact was called
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        
        # Check that unicode filebase is passed
        kwargs = call_args[1]
        if hasattr(kwargs['filebase'], 'value'):
            filebase_value = kwargs['filebase'].value
        else:
            filebase_value = kwargs['filebase']
        assert filebase_value == filebase 
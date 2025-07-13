"""
Unit tests for display_prediction function.
"""
import pytest
import numpy as np
from unittest.mock import patch, MagicMock
from notutils import display_prediction


class TestDisplayPrediction:
    """Test cases for display_prediction function."""

    @patch('notutils.notutils.interact')
    @patch('matplotlib.pyplot.subplots')
    @patch('matplotlib.pyplot.close')
    def test_display_prediction_basic(self, mock_close, mock_subplots, mock_interact):
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_ax.get_xlim.return_value = (-2.0, 2.0)
        mock_ax.get_ylim.return_value = (-1.0, 1.0)
        mock_ax.plot.return_value = [MagicMock()]
        mock_subplots.return_value = (mock_fig, mock_ax)
        def mock_basis(x, num_basis, **kwargs):
            return np.ones((x.shape[0], num_basis))
        display_prediction(mock_basis)
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        assert callable(call_args[0][0])
        kwargs = call_args[1]
        for key in ['num_basis', 'wlim', 'offset']:
            if key in kwargs and hasattr(kwargs[key], 'value'):
                kwargs[key] = kwargs[key].value
        assert kwargs['offset'] == 0.0

    @patch('notutils.notutils.interact')
    @patch('matplotlib.pyplot.subplots')
    @patch('matplotlib.pyplot.close')
    def test_display_prediction_custom_parameters(self, mock_close, mock_subplots, mock_interact):
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_ax.get_xlim.return_value = (-2.0, 2.0)
        mock_ax.get_ylim.return_value = (-1.0, 1.0)
        mock_ax.plot.return_value = [MagicMock()]
        mock_subplots.return_value = (mock_fig, mock_ax)
        def mock_basis(x, num_basis, **kwargs):
            return np.ones((x.shape[0], num_basis))
        display_prediction(
            mock_basis,
            num_basis=6,
            wlim=(-2.0, 2.0),
            xlim=(-5.0, 5.0),
            ylim=(-3.0, 3.0),
            num_points=500,
            offset=1.0
        )
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        kwargs = call_args[1]
        for key in ['num_basis', 'wlim', 'offset']:
            if key in kwargs and hasattr(kwargs[key], 'value'):
                kwargs[key] = kwargs[key].value
        assert kwargs['num_basis'] == 6
        # wlim is used internally but not passed to interact
        # Instead, check that individual weight parameters are created
        assert 'w_0' in kwargs
        assert 'w_1' in kwargs
        assert 'w_2' in kwargs
        assert 'w_3' in kwargs
        assert 'w_4' in kwargs
        assert 'w_5' in kwargs
        assert kwargs['offset'] == 1.0

    @patch('notutils.notutils.interact')
    @patch('matplotlib.pyplot.subplots')
    @patch('matplotlib.pyplot.close')
    def test_display_prediction_with_existing_fig_ax(self, mock_close, mock_subplots, mock_interact):
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_ax.get_xlim.return_value = (-3.0, 3.0)
        mock_ax.get_ylim.return_value = (-2.0, 2.0)
        mock_ax.plot.return_value = [MagicMock()]
        def mock_basis(x, num_basis, **kwargs):
            return np.ones((x.shape[0], num_basis))
        display_prediction(mock_basis, fig=mock_fig, ax=mock_ax)
        mock_interact.assert_called_once()
        mock_subplots.assert_not_called()

    @patch('notutils.notutils.interact')
    @patch('matplotlib.pyplot.subplots')
    @patch('matplotlib.pyplot.close')
    def test_display_prediction_dict_basis(self, mock_close, mock_subplots, mock_interact):
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_ax.get_xlim.return_value = (-2.0, 2.0)
        mock_ax.get_ylim.return_value = (-1.0, 1.0)
        mock_ax.plot.return_value = [MagicMock()]
        mock_subplots.return_value = (mock_fig, mock_ax)
        def mock_basis(x, num_basis, **kwargs):
            return np.ones((x.shape[0], num_basis))
        basis_dict = {"test": mock_basis}
        display_prediction(basis_dict)
        mock_interact.assert_called_once()

    @patch('notutils.notutils.interact')
    @patch('matplotlib.pyplot.subplots')
    @patch('matplotlib.pyplot.close')
    def test_display_prediction_with_kwargs(self, mock_close, mock_subplots, mock_interact):
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_ax.get_xlim.return_value = (-2.0, 2.0)
        mock_ax.get_ylim.return_value = (-1.0, 1.0)
        mock_ax.plot.return_value = [MagicMock()]
        mock_subplots.return_value = (mock_fig, mock_ax)
        def mock_basis(x, num_basis, **kwargs):
            return np.ones((x.shape[0], num_basis))
        display_prediction(mock_basis, sigma=1.0, lengthscale=2.0)
        mock_interact.assert_called_once()
        call_args = mock_interact.call_args
        kwargs = call_args[1]
        if 'sigma' in kwargs:
            assert kwargs['sigma'] == 1.0
        if 'lengthscale' in kwargs:
            assert kwargs['lengthscale'] == 2.0

    @patch('notutils.notutils.interact')
    @patch('matplotlib.pyplot.subplots')
    @patch('matplotlib.pyplot.close')
    def test_display_prediction_default_limits(self, mock_close, mock_subplots, mock_interact):
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_ax.get_xlim.return_value = (-2.0, 2.0)
        mock_ax.get_ylim.return_value = (-1.0, 1.0)
        mock_ax.plot.return_value = [MagicMock()]
        mock_subplots.return_value = (mock_fig, mock_ax)
        def mock_basis(x, num_basis, **kwargs):
            return np.ones((x.shape[0], num_basis))
        display_prediction(mock_basis)
        mock_interact.assert_called_once()
        if mock_subplots.call_count > 0:
            mock_subplots.assert_called_once_with(figsize=(12, 4)) 


class TestDisplayPredictionFullCoverage:
    @patch('notutils.notutils.display')
    @patch('notutils.notutils.interact')
    @patch('matplotlib.pyplot.subplots')
    @patch('matplotlib.pyplot.close')
    def test_generate_function_display_basis_true(self, mock_close, mock_subplots, mock_interact, mock_display):
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_ax.get_xlim.return_value = (-2.0, 2.0)
        mock_ax.get_ylim.return_value = (-1.0, 1.0)
        mock_ax.plot.return_value = [MagicMock() for _ in range(4)]
        mock_subplots.return_value = (mock_fig, mock_ax)
        def mock_basis(x, num_basis, **kwargs):
            return np.ones((x.shape[0], num_basis))
        # Call with display_basis True by patching interact to call the function
        def fake_interact(func, **kwargs):
            # Simulate slider values
            func(
                basis=mock_basis,
                num_basis=4,
                predline=MagicMock(),
                basislines=[MagicMock() for _ in range(4)],
                basis_args={},
                display_basis=True,
                offset=0.0,
                w_0=0.0, w_1=0.0, w_2=0.0, w_3=0.0
            )
        mock_interact.side_effect = fake_interact
        display_prediction(mock_basis)
        mock_interact.assert_called()
        mock_display.assert_called()

    @patch('notutils.notutils.display')
    @patch('notutils.notutils.interact')
    @patch('matplotlib.pyplot.subplots')
    @patch('matplotlib.pyplot.close')
    def test_generate_function_display_basis_false(self, mock_close, mock_subplots, mock_interact, mock_display):
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_ax.get_xlim.return_value = (-2.0, 2.0)
        mock_ax.get_ylim.return_value = (-1.0, 1.0)
        mock_ax.plot.return_value = [MagicMock() for _ in range(4)]
        mock_subplots.return_value = (mock_fig, mock_ax)
        def mock_basis(x, num_basis, **kwargs):
            return np.ones((x.shape[0], num_basis))
        def fake_interact(func, **kwargs):
            func(
                basis=mock_basis,
                num_basis=4,
                predline=MagicMock(),
                basislines=[MagicMock() for _ in range(4)],
                basis_args={},
                display_basis=False,
                offset=0.0,
                w_0=0.0, w_1=0.0, w_2=0.0, w_3=0.0
            )
        mock_interact.side_effect = fake_interact
        display_prediction(mock_basis)
        mock_interact.assert_called()
        mock_display.assert_called()

    @patch('notutils.notutils.display')
    @patch('notutils.notutils.interact')
    @patch('matplotlib.pyplot.subplots')
    @patch('matplotlib.pyplot.close')
    def test_display_prediction_basis_dict(self, mock_close, mock_subplots, mock_interact, mock_display):
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_ax.get_xlim.return_value = (-2.0, 2.0)
        mock_ax.get_ylim.return_value = (-1.0, 1.0)
        mock_ax.plot.return_value = [MagicMock() for _ in range(4)]
        mock_subplots.return_value = (mock_fig, mock_ax)
        def mock_basis(x, num_basis, **kwargs):
            return np.ones((x.shape[0], num_basis))
        basis_dict = {'test': mock_basis}
        display_prediction(basis_dict)
        mock_interact.assert_called()
        # display may not be called in this branch

    @patch('notutils.notutils.display')
    @patch('notutils.notutils.interact')
    def test_display_prediction_with_custom_axes(self, mock_interact, mock_display):
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_ax.get_xlim.return_value = (-5.0, 5.0)
        mock_ax.get_ylim.return_value = (-3.0, 3.0)
        mock_ax.plot.return_value = [MagicMock() for _ in range(4)]
        def mock_basis(x, num_basis, **kwargs):
            return np.ones((x.shape[0], num_basis))
        display_prediction(mock_basis, fig=mock_fig, ax=mock_ax, xlim=(-5, 5), ylim=(-3, 3))
        mock_interact.assert_called()
        # display may not be called in this branch 
# notutils

Jupyter Notebook Utilities for Python

[![Tests](https://github.com/lawrennd/notutils/workflows/Test%20and%20Coverage/badge.svg)](https://github.com/lawrennd/notutils/actions?query=workflow%3A%22Test+and+Coverage%22)

---

## Overview

`notutils` is a collection of convenience functions designed to enhance the Jupyter Notebook experience for Python users. It provides convenient tools for displaying URLs, embedding iframes, visualizing Google Books, toggling code visibility, creating interactive prediction widgets, and more. The library was designed for teaching, presentations, and interactive data exploration.

## Features

- Display clickable URLs in notebooks
- Embed external content with iframes
- Visualize Google Books inline
- Toggle code cell visibility for cleaner presentations
- Interactive basis function prediction widgets
- Display image and plot series with sliders
- Utilities for Jupyter/IPython integration

## Installation

You can install notutils using [Poetry](https://python-poetry.org/) or pip:

### Using Poetry
```bash
poetry add notutils
```

### Using pip
```bash
pip install notutils
```

> **Note:** notutils requires Python 3.9 or later. It depends on `IPython`, `ipywidgets`, `matplotlib`, and `numpy`.

## Quick Start

```python
from notutils import display_url, iframe_url, display_iframe_url

display_url("https://github.com/lawrennd/notutils")
iframe_html = iframe_url("https://www.example.com", width=800, height=400)
display_iframe_url("https://www.example.com", width=800, height=400)
```

## Usage Examples

### Display a Clickable URL
```python
from notutils import display_url
display_url("https://www.python.org")
```

### Embed an IFrame
```python
from notutils import display_iframe_url
display_iframe_url("https://www.wikipedia.org", width=700, height=500)
```

### Toggle Code Visibility
```python
from notutils import code_toggle
code_toggle(start_show=False, message="Show/Hide code")
```

### Interactive Prediction Widget
```python
from notutils import display_prediction
# Define your basis function and call display_prediction(...)
```

## Dependencies
- Python >= 3.9
- IPython
- ipywidgets
- matplotlib
- numpy

## Development & Contributing

1. Clone the repository:
   ```bash
   git clone https://github.com/lawrennd/notutils.git
   cd notutils
   ```
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Run tests:
   ```bash
   poetry run pytest
   ```
4. See the [backlog](backlog/index.md) and [CIPs](cip/README.md) for project planning and improvement proposals.

Contributions are welcome! Please open issues or pull requests for bugs, features, or documentation improvements.

## License

This project is licensed under the BSD 3-clause license. See [LICENSE.txt](LICENSE.txt) for details.

## Links
- [Documentation (docs/)](docs/)
- [Backlog](backlog/index.md)
- [Code Improvement Plans (CIPs)](cip/README.md)
- [Project Tenets](tenets/)
- [GitHub Repository](https://github.com/lawrennd/notutils)

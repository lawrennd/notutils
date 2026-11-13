#!/usr/bin/env python
"""Backwards-compatible setup entrypoint.

Package metadata and builds are defined in ``pyproject.toml`` (PEP 621 + hatchling).
Prefer::

    pip install -e .
    uv sync
    uv build
"""

from setuptools import setup

if __name__ == "__main__":
    setup()

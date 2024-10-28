# Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # Zakładając, że twoje moduły są w katalogu nadrzędnym
# -- Project information -----------------------------------------------------

project = 'Nazwa Projektu'  # Zmień na nazwę swojego projektu
author = 'Twoje Imię'       # Zmień na swoje imię
release = '0.1'             # Zmień na aktualną wersję projektu

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # Włącza automatyczne dokumentowanie
    'sphinx.ext.napoleon',  # Obsługuje style docstringów Google i NumPy
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'  # Możesz zmienić motyw na inny, jeśli chcesz
html_static_path = ['_static']

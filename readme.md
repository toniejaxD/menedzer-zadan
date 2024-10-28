# Nazwa Projektu

Menedżer zadań - prosty projekt do zarządzania zadaniami.

## Instalacja

1. Sklonuj repozytorium: 
   ```bash
   git clone https://github.com/toniejaxD/menedzer-zadan

2. Przejdź do katalogu projektu (to zależy od zapisu danego projektu!):

   cd menedzer-zadan

3. Utwórz i aktywuj wirtualne środowisko (na systemie Windows):

   python -m venv venv
   
   venv\Scripts\activate

5. Zainstaluj wymagane zależności:

   pip install -r requirements.txt

## Użycie

1. Uruchom aplikację:

   python main.py

## Dokumentacja

   Dokumentacja projektu dostępna jest na stronie GitHub: Menedżer Zadań. 
   Szczegóły dotyczące struktury projektu, 
   architektury oraz sposobu rozbudowy znajdziesz w pliku docs/.

   Żeby utworzyć takiego dokumentu trzeba wpisać takiego komendy:
   
   1. Instalacja Sphinx:

         pip install sphinx

   3. Inicjalizacja Sphinx w projekcie:
      
         sphinx-quickstart

      Utworzenie folderu docs:

      sphinx-apidoc -o docs .


jeśli nie wygenerowało plik conf.py oraz index.rst, trzeba go utworzyć pliku w folderze docs i wpisać:

## conf.py:

#Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
#-- Project information -----------------------------------------------------

project = 'Nazwa Projektu'
author = 'Twoje Imię'
release = '0.1'

#-- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # Enable docstring extraction
    'sphinx.ext.napoleon',  # Support for Google style docstrings
]

templates_path = ['_templates']
exclude_patterns = []

#-- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']


## index.rst:

.. Project name documentation master file, created by
   sphinx-quickstart on date.

Welcome to Project Name's documentation!
=========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   main
   zadania

Indices and tables
===================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Po stworzeniu 2 plików trzeba wpisać do komendy:
cd docs
sphinx-build -b html . _build/html

## Autor

   Karol Kołodyński

## Licencja

   Ten projekt jest objęty licencją MIT - zobacz plik [LICENSE](./LICENSE) po więcej szczegółów.

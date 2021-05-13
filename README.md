# ls-util

## Installing Requirements

Prefered to create a Virtual environment and run

`pip install requirements.txt`

*python 3.8.5 and Linux OS recommended*

## To run the ls program

`python3 main.py`

## Generating sphinx documentation

Navigate to docs directory

`cd docs`

*this is the directory we create to seperate code from docs*

To initialize Sphinx 

`sphinx-quickstart`

*already initialized files are present, run the above command when you are creating your own documentation for the first time*

*modify the index.rst as needed*

To generate HTML Document

`make html`

*other outputs are available too, refer sphinx documentation*

the output is populated to `_build` directory

Locating the Output files

`cd _build`

To view the index file

`firefox index.html`

*use the browser of your choice*


## Modifying the HTML Style

[sphinx-themes](https://sphinx-themes.org/)

*Example:*

To install *Read The Docs* template

`pip install sphinx-rtd-theme`

open the `conf.py` file under `docs` directory

set the variable `html_theme` to the installed theme

`html_theme = 'sphinx_rtd_theme'`
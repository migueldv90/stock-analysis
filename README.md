# Stock Analysis
*   Python 3.9.6

## Install Dependencies - System

**commands**

    brew update
    brew upgrade
    brew install git
    brew install python

**~/.zshrc**

    export PATH="/usr/local/opt/python/libexec/bin:$PATH"

## Virtual Environment - Python

virtualenv & virtualenvwrapper

**install**

    pip install flake8 --upgrade
    pip install virtualenv --upgrade
    pip install virtualenvwrapper --upgrade

**~/.zshrc**

    export PROJECT_HOME=$HOME/development
    export WORKON_HOME=$HOME/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=$(which python3)
    export VIRTUALENVWRAPPER_VIRTUALENV=$(which virtualenv)
    source $(which virtualenvwrapper.sh)

**commands**

    workon
    workon stock-analysis
    rmvirtualenv stock-analysis
    mkvirtualenv --python=python3 stock-analysis

## PIP

**commands**

    pip install --upgrade pip

    pip install -r requirements.txt
    pip uninstall -r requirements.txt

    pip freeze > requirements.txt

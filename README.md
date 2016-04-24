# ptd - Python TODO List

[![Build Status](https://travis-ci.org/tomasboccardo/ptd.svg?branch=develop)](https://travis-ci.org/tomasboccardo/ptd)

## Requisites

    python ------------------> 3.x

## Setting up development environment

### Installing virtualenvwrapper

Check [this link](http://virtualenvwrapper.readthedocs.org/en/latest/install.html) to install `virtualenvwrapper` for your OS

### Setting up virtualenv

    mkvirtualenv --python=/usr/bin/python3 ptd-env
    pip install -r requirements.txt

### Running the project

    # To run specific command
    ptd.sh <command>
    # To run GUI mode
    ptd.sh gui

### Running tests

    py.test test/


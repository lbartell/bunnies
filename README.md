FOOBAR Exercises
================

This contains my solutions to the Google FooBar coding challenges.

There are multiple challenges of variable difficulty across 5 levels. I completed 
some but not all of the challenges (up to the first challenge in level 4). 
Each challenge lives in its own subfolder with associated readme.

Summary of challenges
- Level 1
    - `/cake/`
- Level 2
    - `/elevator/`
    - `/salute/`
- Level 3
    - `/fuel/`
    - `/baby/`
    - `/staircase/`
- Level 4
    - `/running/` (not a successful submission)

For more info about FooBar:
https://medium.com/plutonic-services/things-you-should-know-about-google-foobar-invitation-703a535bf30f


# Dev setup

This code runs in a python 2.7 environment with `poetry`-based dependency and package management. 
 

Suggested setup:
1. Clone this repo and move (`cd`) to the repo root
1. Setup a python 2.7 env
    - Install [pyenv](https://github.com/pyenv/pyenv)
    - Install python 2.7: `pyenv install 2.7.17`
    - Set python version (from repo root): `pyenv local 2.7.17`
1. Setup virtual env 
    - Install [poetry](https://python-poetry.org/)
    - Create venv (from repo root): `poetry install`
    - Activate the venv: `source .venv/bin/activate`

# Tests

This code has `unittest`-based tests with a `nosetest` runner.

Test can be run via the command line:
- Run all tests: `nosetests`
- Run tests in a particular subfolder, e.g.,: `nosetests baby`

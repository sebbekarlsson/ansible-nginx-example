#!/bin/bash

virtualenv -p $(which python3) ./venv
source ./venv/bin/activate
cd tests
python setup.py develop
cd ..
pytest
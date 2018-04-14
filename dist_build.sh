#!/bin/bash

# Automate the process of running a dist build for pyusbmodule
#
# author: mikeqin
# email: laigui@gmail.com
rm -f dist/*
python3 setup.py sdist
python3 setup.py bdist_wheel
twine upload dist/*
sudo pip3 install -U pyusbmodule
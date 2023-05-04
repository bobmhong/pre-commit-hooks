#!/bin/bash

requirements_file="requirements-dev.txt"

python scripts/check_requirements.py $requirements_file
if [ $? -eq 1 ]
then
    echo Installing missing packages...
    pip install -r $requirements_file
fi

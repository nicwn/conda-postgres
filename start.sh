#!/bin/bash

# Create the anaconda-vol folder if it doesn't exist
mkdir -p anaconda-vol

# Copy only .py and .ipynb files from the current directory to the anaconda-vol folder
find . -maxdepth 1 -type f \( -iname \*.py -o -iname \*.ipynb \) -exec cp {} anaconda-vol/ \;

# Run docker compose
docker compose up --build

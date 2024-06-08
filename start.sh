#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if Python is installed
if ! command_exists python; then
    echo "Python3 is not installed. Please install Python3 to proceed."
    exit 1
fi

# Function to check if a Python package is installed
check_and_install() {
    package=$1
    if ! python -c "import $package" &> /dev/null; then
        echo "$package not found. Installing..."
        pip install $package
    else
        echo "$package is already installed."
    fi
}

# Check and install necessary packages
check_and_install pygame

# Run the game
python game/start.py

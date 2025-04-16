#!/bin/bash

set -e

echo "Creating and activating the virtual environment"
python3 -m venv venv
source venv/bin/activate

echo "Installing the inventory api python client"
python3 -m pip install project-kessel-inventory-api-grpc-python --extra-index-url https://buf.build/gen/python

echo "Installing package locally"
pip install .

echo "Copying files to src directory for buf validation"
mkdir -p src/buf/validate
touch src/buf/__init__.py
touch src/buf/validate/__init__.py
cp -r venv/lib/python*/site-packages/buf/validate/* src/buf/validate

echo "Copying files to src directory"
mkdir -p src/kessel/inventory/
touch src/kessel/inventory/__init__.py
cp -r venv/lib/python*/site-packages/kessel/inventory/* src/kessel/inventory/

echo "Deactivating and removing the virtual environment..."
deactivate

echo "Removing the virtual environment"
rm -rf "venv"

echo "Python client successfully updated"

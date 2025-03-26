#!/bin/bash

set -e

GITHUB_REPO_URL="https://github.com/project-kessel/inventory-api"
PROTO_FOLDER="api/kessel/inventory/v1beta1"
TEMP_DIR=$(mktemp -d)
VENV_DIR="$TEMP_DIR/venv"
OUTPUT_DIR=$(pwd)

echo "Creating and activating the virtual environment"
 python3 -m venv venv
 source venv/bin/activate

 echo "Installing the inventory api python client"
 python3 -m pip install project-kessel-inventory-api-grpc-python --extra-index-url https://buf.build/gen/python
echo "Copying files to necessary directory for buf validation files"
 mkdir -p src/buf/validate
 cp -r venv/lib/python*/site-packages/buf/validate/* src/buf/validate

echo "Copying files to necessary directory for buf validation files"
mkdir -p src/buf/validate
touch src/buf/__init__.py
touch src/buf/validate/__init__.py
cp -r venv/lib/python*/site-packages/buf/validate/* src/buf/validate

echo "Copying files to necessary directory"
mkdir -p src/kessel/inventory/v1beta1
cp -r venv/lib/python*/site-packages/kessel/inventory/v1/* src/kessel/inventory/v1/
cp -r venv/lib/python*/site-packages/kessel/inventory/v1beta1/* src/kessel/inventory/v1beta1/
cp -r venv/lib/python*/site-packages/kessel/inventory/v1beta2/* src/kessel/inventory/v1beta2/


echo "Deactivating and removing the virtual environment..."
deactivate

echo "Removing the virtual environment"
rm -rf "venv"


echo "python client successfully updated"

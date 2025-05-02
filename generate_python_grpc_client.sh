#!/bin/bash

set -e

BUF_MODULE="buf.build/project-kessel/inventory-api"
PROTO_OUT_DIR="proto"
PYTHON_OUT_DIR="src"
VENV_DIR=".venv"

echo "Cleaning up old generated files..."
rm -rf "${PROTO_OUT_DIR}"
rm -rf "${PYTHON_OUT_DIR}/kessel/inventory"

echo "Creating proto and python output directories..."
mkdir -p "${PROTO_OUT_DIR}"
mkdir -p "${PYTHON_OUT_DIR}"

echo "Exporting protos from Buf.build..."
buf export "${BUF_MODULE}" --output "${PROTO_OUT_DIR}"

echo "Setting up a fresh virtual environment..."
python3 -m venv "${VENV_DIR}"
source "${VENV_DIR}/bin/activate"

echo "Installing necessary tools inside the virtual environment..."
pip install --upgrade pip

pip install .
pip install "grpcio-tools>=1.70.0"

echo "Generating Python gRPC client code from protos..."
python -m grpc_tools.protoc \
    --proto_path="${PROTO_OUT_DIR}" \
    --python_out="${PYTHON_OUT_DIR}" \
    --grpc_python_out="${PYTHON_OUT_DIR}" \
    $(find "${PROTO_OUT_DIR}" -name "*.proto")

echo "Deactivating virtual environment..."
deactivate

echo "Removing virtual environment..."
rm -rf "${VENV_DIR}"
rm -rf "${PROTO_OUT_DIR}"
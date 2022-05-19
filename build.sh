#!/bin/sh
python -m grpc_tools.protoc -I protos --python_out=grpc-app --grpc_python_out=grpc-app  protos/*.proto

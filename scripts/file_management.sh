#!/bin/bash

folder
mkdir -p output_models
mv .pkl output_models/

rm -rf pycache
rm -rf.ipynb_checkpoints

echo "Files organized successfully."
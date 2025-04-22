#!/bin/bash

current_dir=$(pwd)

mkdir -p "$current_dir/output_models"

mv "$current_dir/"/*.pkl "$current_dir/output_models/"


echo "Files organized successfully."

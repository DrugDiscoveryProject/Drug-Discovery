#!/bin/bash

cd Train_Notebook/

for notebook in *.ipynb
do
  echo "Training model with $notebook"
  jupyter nbconvert --to notebook --execute "$notebook" --output "output_$notebook"
done

echo "All models have been trained."
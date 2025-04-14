#!/bin/bash

cd Train_Model/

for model in *.pkl
do
  echo "Evaluating model: $model"
  python evaluate_model.py --model "$model" --output "results_$model.txt"
done

echo "Model evaluation complete."

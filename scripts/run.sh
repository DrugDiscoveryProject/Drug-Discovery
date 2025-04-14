#!/bin/bash

# Get the base directory (i.e., project root)
BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"

# Define source and destination paths
SRC="$BASE_DIR/Train_Model"
DEST="$BASE_DIR/Frontend/Models"

# Create Models directory if it doesn't exist
mkdir -p "$DEST"

# Copy contents from Train_Model to Frontend/Models
cp -r "$SRC"/* "$DEST"

# Navigate to Frontend folder
cd "$BASE_DIR/Frontend" || exit

# Run Streamlit
streamlit run main.py

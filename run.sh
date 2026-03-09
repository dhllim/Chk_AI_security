#!/bin/bash

echo "Installing required dependencies..."
pip install -r requirements.txt

echo "Starting AI Security Controls Dashboard..."
streamlit run app.py

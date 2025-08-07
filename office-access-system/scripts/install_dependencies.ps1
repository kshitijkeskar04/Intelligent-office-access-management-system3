#!/bin/bash

# Ensure we're in bash and stop on error
Set-Variable -e  # Stop script on error
Set-Variable -x  # Print each command (for debugging)

# 1. Install Python dependencies
printf "\n📦 Installing Python packages from ../requirements.txt...\n"
python3 -m pip install --upgrade pip
python3 -m pip install -r ../requirements.txt

# 2. Instructions for Windows users
printf "\n⚠️  Windows Setup Instructions (manual installation required):\n"
printf "------------------------------------------------------------\n"
printf "• Python 3.8+ → https://www.python.org/downloads/\n"
printf "• Microsoft Visual C++ Build Tools → https://visualstudio.microsoft.com/visual-cpp-build-tools/\n"
printf "• OpenCV (Python) → pip install opencv-python\n\n"

# 3. Elasticsearch installation (Windows)
printf "🔍 Elasticsearch for Windows:\n"
printf "Download from: https://www.elastic.co/downloads/elasticsearch\n"
printf "After extracting, run: bin\\elasticsearch.bat\n\n"

printf "✅ Installation script completed successfully!\n"

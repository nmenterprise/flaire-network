#!/bin/bash

# Install system dependencies
apt-get update
apt-get install -y libdbus-1-dev cmake

# Install Python dependencies
pip install -r requirements.txt

# Run any additional build commands
# Example: python manage.py collectstatic --noinput

# Create a directory for static files if not exists
mkdir -p staticfiles

# Build static files
python manage.py collectstatic --noinput

echo "Build complete!"

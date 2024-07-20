#!/bin/bash

# Update package list and install dependencies
apt-get update
apt-get install -y \
  libdbus-1-dev \
  cmake \
  meson \
  ninja-build \
  python3-pip

# Install Python dependencies
pip install -r requirements.txt

# Build dbus-python
cd /tmp
git clone https://github.com/dbus/dbus-python.git
cd dbus-python
git checkout 1.3.2  # Ensure you are using the correct version
meson setup build
meson compile -C build
meson install -C build

echo "Build complete!"

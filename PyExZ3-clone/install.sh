#!/bin/bash

# Set installation path
INSTALL_PATH="$HOME/DSE"
REPO_URL="https://github.com/555shivv/tool.git"
TOOL_DIR="$INSTALL_PATH/PyExZ3-clone"
VENV_DIR="$TOOL_DIR/.venv"
SCRIPT_FILE="$TOOL_DIR/dse_run.sh"

echo "Installing DSE(Dynamic Symbolic Excecution) tool (PyExZ3)..."

# Ensure Python 3 and Git are installed
if ! command -v python3 &>/dev/null; then
    echo "Error: Python3 is not installed!"
    exit 1
fi

if ! command -v git &>/dev/null; then
    echo "Error: Git is not installed!"
    exit 1
fi

# Create the installation directory if it doesn't exist
mkdir -p "$INSTALL_PATH"

# Clone PyExZ3 if not already cloned
if [ ! -d "$TOOL_DIR" ]; then
    echo "Cloning PyExZ3 repository..."
    git clone "$REPO_URL" "$TOOL_DIR" || { echo "Error: Failed to clone repository!"; exit 1; }
else
    echo "PyExZ3 repository already exists. Pulling latest changes..."
    cd "$TOOL_DIR" && git pull
fi

cd "$TOOL_DIR" || { echo "Error: Could not access tool directory!"; exit 1; }

# Create and activate the virtual environment
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR" || { echo "Error: Failed to create virtual environment!"; exit 1; }
fi

echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate" || { echo "Error: Failed to activate virtual environment!"; exit 1; }

# Install dependencies
echo "Installing dependencies..."
pip install -U pip
pip install -q z3 || { echo "Error: Failed to install z3!"; exit 1; }

# Ensure dse_run.sh is executable
if [ -f "$SCRIPT_FILE" ]; then
    echo "Setting execute permissions for dse_run.sh..."
    chmod +x "$SCRIPT_FILE" || { echo "Error: Failed to set execute permissions for dse_run.sh!"; exit 1; }
else
    echo "Warning: dse_run.sh not found. Ensure it is placed in $TOOL_DIR."
fi

echo "Installation completed successfully."


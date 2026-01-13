#!/bin/bash

# Script to find all CLAUDE.md files in frontend and backend folders
# and create copies named AGENTS.md

# Set the base directory (parent directory of scripts)
BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"

# Parse arguments
REVERSE=0
if [[ "$1" == "--reverse" ]]; then
    REVERSE=1
fi

# Function to process files based on direction
process_files() {
    local search_dir="$1"

    # Find all relevant files recursively
    if [ $REVERSE -eq 0 ]; then
        # Normal: CLAUDE.md -> AGENTS.md
        find "$search_dir" -name "CLAUDE.md" -type f | while read -r src_file; do
            dir_path=$(dirname "$src_file")
            dest_file="$dir_path/AGENTS.md"
            cp -f "$src_file" "$dest_file"
            if [ $? -eq 0 ]; then
                echo "Created/Updated: $dest_file"
            else
                echo "Error copying: $src_file to $dest_file"
            fi
        done
    else
        # Reverse: AGENTS.md -> CLAUDE.md
        find "$search_dir" -name "AGENTS.md" -type f | while read -r src_file; do
            dir_path=$(dirname "$src_file")
            dest_file="$dir_path/CLAUDE.md"
            cp -f "$src_file" "$dest_file"
            if [ $? -eq 0 ]; then
                echo "Created/Updated: $dest_file"
            else
                echo "Error copying: $src_file to $dest_file"
            fi
        done
    fi
}

# Check if frontend directory exists and process it
if [ -d "$BASE_DIR/app" ]; then
    echo "Searching in app directory..."
    process_files "$BASE_DIR/app"
else
    echo "Warning: app directory not found"
fi

# Check if backend directory exists and process it
if [ -d "$BASE_DIR/ui" ]; then
    echo "Searching in ui directory..."
    process_files "$BASE_DIR/ui"
else
    echo "Warning: ui directory not found"
fi

if [ -d "$BASE_DIR/varro" ]; then
    echo "Searching in varro directory..."
    process_files "$BASE_DIR/varro"
else
    echo "Warning: varro directory not found"
fi

echo "Done!"
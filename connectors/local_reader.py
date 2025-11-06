import os

def list_files(input_dir):
    files = []
    for root, _, filenames in os.walk(input_dir):
        for name in filenames:
            # Only include .txt files (case-insensitive)
            if name.lower().endswith(".txt"):
                path = os.path.join(root, name)
                files.append({"path": path})
    return files

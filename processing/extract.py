import os

def extract_texts(files):
    """
    Reads text content from the given file paths.
    Returns a list of dictionaries with file path and text.
    """
    out = []
    for f in files:
        path = f['path']
        text = ""

        # Handle plain text files
        if path.lower().endswith(".txt"):
            try:
                with open(path, "r", encoding="utf-8") as infile:
                    text = infile.read()
            except Exception as e:
                print(f"⚠️ Error reading {path}: {e}")
                text = ""

        # Future: add PDF or DOCX extraction here if needed

        out.append({"path": path, "text": text})
    return out

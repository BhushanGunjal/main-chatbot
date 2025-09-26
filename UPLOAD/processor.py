import os

UPLOAD_DIR = "./uploads"

def save_file(file) -> str:
    """
    Save uploaded file locally and return path.
    """
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path

def extract_text(file_path: str) -> str:
    """
    Dummy extractor for now. Later: add PDF, DOCX, TXT parsing.
    """
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

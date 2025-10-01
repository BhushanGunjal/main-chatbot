import os
import nltk
import tiktoken
import pdfplumber
from docx import Document

UPLOAD_DIR = "./uploads"

# To ignore if already present
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
encoding = tiktoken.get_encoding("cl100k_base")



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
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
        
    elif ext == ".pdf":
        text = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
        return "\n\n".join(text)
    
    elif ext == ".docx":
        doc = Document(file_path)
        for para in doc.paragraphs:
            if para.text.strip():
                text.append(para.text)
        return "\n\n".join(text)



def count_tokens(text: str) -> int:
    return len(encoding.encode(text))



def chunk_text(text: str, filename: str = "unknown", max_tokens: int = 50, overlap_sentences: int = 1) -> list[str]:
    """
    Break text into chunks: paragraph -> sentences -> tokens
    """
    paragrahs = text.split("\n\n")
    chunks = []
    chunk_index = 0

    for para in paragrahs:
        if not para.strip():
            continue

        if count_tokens(para) <= max_tokens:
            chunks.append(
                {
                    "id": f"{filename}_{chunk_index}", 
                    "text": para.strip(),
                    "metadata": {
                        "filename" : filename,
                        "chunk_index": chunk_index,
                        "token_count": count_tokens(para.strip())
                        }
                })

        else:

            sentences = nltk.sent_tokenize(para)
            current_chunk = []
            current_len = 0

            for i, sent in enumerate(sentences):
                sent_len = count_tokens(sent)

                if current_len + sent_len > max_tokens:
                    chunktext = " ".join(current_chunk).strip() 
                    chunks.append({
                        "id": f"{filename}_{chunk_index}",
                        "text": chunktext,
                        "metadata": {
                            "filename": filename,
                            "chunk_index": chunk_index,
                            "token_count": current_len
                            }
                        })
                    chunk_index += 1


                    overlap = sentences[max(0, i - overlap_sentences):i]
                    current_chunk = overlap + [sent]
                    current_len = sum(count_tokens(s) for s in current_chunk)
                    
                else:

                    current_chunk.append(sent)
                    current_len += sent_len


            if current_chunk:
                chunktext = " ".join(current_chunk).strip()
                chunks.append({
                    "id": f"{filename}_{chunk_index}",
                    "text": chunktext,
                    "metadata": {
                        "filename": filename,
                        "chunk_index": chunk_index,
                        "token_count": current_len
                    }
                })
                chunk_index += 1


    print("Chunks: ", chunks) 
    return chunks
        




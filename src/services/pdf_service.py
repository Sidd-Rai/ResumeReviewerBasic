import pymupdf as pp

def read_pdf_text(pdf_bytes: bytes) -> str:
    doc = pp.open(stream=pdf_bytes, filetype="pdf")

    text = ""
    for page in doc:
        text += page.get_text()

    doc.close()
    return text
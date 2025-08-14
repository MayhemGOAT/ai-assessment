import sys, fitz, os, pathlib
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models
from app.services.question_gen import generate_all

def extract_text(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    return "\n".join(page.get_text() for page in doc)

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/ingest_pdf.py <path_to_pdf>"); return
    pdf = sys.argv[1]
    if not os.path.exists(pdf): print("File not found:", pdf); return
    text = extract_text(pdf)
    qs = generate_all(text, topic=None, difficulty="medium", num_mcq=3, num_desc=2, num_code=1)
    db: Session = SessionLocal()
    try:
        qids = []
        for g in qs:
            q = models.Question(**g); db.add(q); db.flush(); qids.append(q.id)
        db.commit()
        a = models.Assessment(title=f"Ingested from {pathlib.Path(pdf).name}", duration=30, question_ids=qids, status="published")
        db.add(a); db.commit()
        print("Created assessment:", a.id); print("Questions:", qids)
    finally:
        db.close()

if __name__ == "__main__": main()

# AI-Powered Assessment System (MVP)

- FastAPI backend, PostgreSQL, Next.js frontend, Adminer, Docker Compose
- PDF ingestion script creates questions and a published assessment
- OpenAPI stub + Postman sample
- Works in stub mode (no keys required)

## Run with Docker
```bash
cp .env.example .env
docker compose up --build
```
Services:
- Frontend: http://localhost:3000
- Backend (docs): http://localhost:8000/docs
- Adminer (DB UI): http://localhost:8080

## Ingest a PDF
```bash
cd backend
python scripts/ingest_pdf.py ../data/example.pdf
```

## Push to Git
```bash
git init
git add .
git commit -m "Initial commit: AI Assessment MVP"
git branch -M main
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main
```

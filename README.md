# AI Assessment Platform

An AI-powered assessment generation platform with a **FastAPI backend**, **Next.js frontend**, and **PostgreSQL** database, running in Docker for easy deployment.

## 📌 Features
- Generate multiple-choice, descriptive, and coding questions using AI.
- Web-based frontend built with **Next.js**.
- REST API backend built with **FastAPI**.
- Persistent database using **PostgreSQL**.
- Adminer UI for database management.

---

## 🗂 Project Structure
```
ai-assessment/
├── backend/         # FastAPI app code
├── frontend/        # Next.js frontend
├── data/            # Data storage (if any)
├── db/              # Database migrations/config
├── openapi/         # API documentation
├── docker-compose.yml
├── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [GitHub Codespaces](https://docs.github.com/en/codespaces) *(optional, for cloud dev)*
- GitHub account

---

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/ai-assessment.git
cd ai-assessment/ai-assessment
```

---

### 3️⃣ Set up Environment Variables
Create a `.env` file:
```bash
cp .env.example .env
```
Edit it with your **backend** and **frontend** public URLs (found in GitHub Codespaces’ “Ports” tab):
```env
BACKEND_URL=https://<your-8000-port-URL>/
CORS_ORIGINS=https://<your-3000-port-URL>/
```

---

### 4️⃣ Build and Run
```bash
docker compose up --build
```

---

### 5️⃣ Access Services
| Service      | URL (example in Codespaces)                                    |
|--------------|---------------------------------------------------------------|
| **Frontend** | `https://<your-3000-port-URL>/`                                |
| **Backend**  | `https://<your-8000-port-URL>/docs` (Swagger API docs)         |
| **Database** | `localhost:5432` (PostgreSQL)                                  |
| **Adminer**  | `https://<your-8080-port-URL>/` (UI for DB management)         |

---

## 🧪 Testing AI Generation
Once the app is running:
1. Open the frontend in your browser.
2. Use the **Generate Questions** feature.
3. Example request (backend):
```bash
POST /admin/questions/generate
{
  "source_text": "Machine learning is a subset of AI.",
  "num_mcq": 2,
  "num_desc": 1,
  "num_code": 1,
  "topic": "AI Basics",
  "difficulty": "medium"
}
```

---

## 📦 Stopping Services
```bash
docker compose down
```

---

## 🔐 Notes
- **Do not commit `.env`** files with secrets.
- Commit your changes to GitHub to avoid losing progress in Codespaces:
```bash
git add .
git commit -m "Setup env and config changes"
git push
```

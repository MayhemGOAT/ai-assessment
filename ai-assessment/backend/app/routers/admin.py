from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from ..database import get_db
from .. import models
from ..schemas import AssessmentCreate, AssessmentOut, QuestionOut, GenerateQuestionsRequest, ReviewQuestionsOut
from ..services.question_gen import generate_all

router = APIRouter(prefix="/admin", tags=["admin"])

@router.post("/assessments/create", response_model=AssessmentOut)
def create_assessment(payload: AssessmentCreate, db: Session = Depends(get_db)):
    a = models.Assessment(title=payload.title, duration=payload.duration, question_ids=payload.question_ids, status="published")
    db.add(a); db.commit(); db.refresh(a)
    return AssessmentOut(id=a.id, title=a.title, duration=a.duration, question_ids=a.question_ids or [], status=a.status)

@router.post("/questions/generate", response_model=List[QuestionOut])
def generate_questions(req: GenerateQuestionsRequest, db: Session = Depends(get_db)):
    generated = generate_all(req.source_text, req.topic, req.difficulty, req.num_mcq, req.num_desc, req.num_code)
    out = []
    for g in generated:
        q = models.Question(**g); db.add(q); db.flush()
        out.append(QuestionOut(id=q.id, **g))
    db.commit()
    return out

@router.get("/questions/review", response_model=ReviewQuestionsOut)
def review_questions(db: Session = Depends(get_db)):
    qs = db.query(models.Question).limit(20).all()
    sample = [
        QuestionOut(
            id=q.id, type=q.type, question=q.question, options=q.options, correct_answer=q.correct_answer,
            explanation=q.explanation, topic=q.topic, difficulty=q.difficulty, source=q.source,
            auto_generated=(str(q.auto_generated).lower() == "true")
        ) for q in qs
    ]
    total = db.query(models.Question).count()
    return ReviewQuestionsOut(total=total, sample=sample)

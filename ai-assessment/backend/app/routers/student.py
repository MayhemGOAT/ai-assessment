from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from ..database import get_db
from .. import models
from ..schemas import AssessmentOut, StartAssessment, SubmitPayload, SubmissionOut
from ..services.scoring import score_assessment
from ..services.feedback import generate_feedback

router = APIRouter(tags=["student"])

@router.get("/assessments/available", response_model=list[AssessmentOut])
def list_available(db: Session = Depends(get_db)):
    items = db.query(models.Assessment).filter(models.Assessment.status=="published").all()
    return [AssessmentOut(id=i.id, title=i.title, duration=i.duration, question_ids=i.question_ids or [], status=i.status) for i in items]

@router.post("/assessments/{assessment_id}/start")
def start_assessment(assessment_id: UUID, payload: StartAssessment, db: Session = Depends(get_db)):
    a = db.query(models.Assessment).get(assessment_id)
    if not a: raise HTTPException(404, "Assessment not found")
    return {"message": "Timer started", "assessment_id": str(a.id)}

@router.post("/assessments/{assessment_id}/submit", response_model=SubmissionOut)
def submit_assessment(assessment_id: UUID, payload: SubmitPayload, db: Session = Depends(get_db)):
    a = db.query(models.Assessment).get(assessment_id)
    if not a: raise HTTPException(404, "Assessment not found")
    qids = a.question_ids or []
    if not qids: raise HTTPException(400, "Assessment has no questions")
    qs = db.query(models.Question).filter(models.Question.id.in_(qids)).all()
    qdicts = [{"id": q.id, "type": q.type, "question": q.question, "options": q.options, "correct_answer": q.correct_answer} for q in qs]
    answers = [{"question_id": str(s.question_id), "answer": s.answer} for s in payload.answers]
    score, details = score_assessment(qdicts, answers)
    feedback = generate_feedback(details, qdicts)
    sub = models.Submission(user_id=payload.user_id, assessment_id=a.id, score=score, feedback=feedback, details={"items": details})
    db.add(sub); db.commit(); db.refresh(sub)
    return {"id": sub.id, "score": sub.score, "feedback": sub.feedback, "details": sub.details}

@router.get("/submissions/{submission_id}/result", response_model=SubmissionOut)
def get_result(submission_id: UUID, db: Session = Depends(get_db)):
    s = db.query(models.Submission).get(submission_id)
    if not s: raise HTTPException(404, "Submission not found")
    return {"id": s.id, "score": s.score, "feedback": s.feedback, "details": s.details}

@router.get("/submissions/history")
def history(user_id: UUID | None = None, db: Session = Depends(get_db)):
    q = db.query(models.Submission)
    if user_id: q = q.filter(models.Submission.user_id==user_id)
    return [{"id": s.id, "score": s.score, "submitted_at": s.submitted_at, "assessment_id": s.assessment_id} for s in q.order_by(models.Submission.submitted_at.desc()).limit(50)]

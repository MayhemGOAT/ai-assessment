from pydantic import BaseModel
from typing import List, Optional, Any
from uuid import UUID

class QuestionCreate(BaseModel):
    type: str
    question: str
    options: Optional[List[str]] = None
    correct_answer: Optional[str] = None
    explanation: Optional[str] = None
    topic: Optional[str] = None
    difficulty: Optional[str] = None
    source: Optional[str] = None
    auto_generated: bool = True

class QuestionOut(QuestionCreate):
    id: UUID

class AssessmentCreate(BaseModel):
    title: str
    duration: int
    question_ids: List[UUID] = []

class AssessmentOut(AssessmentCreate):
    id: UUID
    status: str

class StartAssessment(BaseModel):
    user_id: Optional[UUID] = None

class SubmitAnswer(BaseModel):
    question_id: UUID
    answer: Any

class SubmitPayload(BaseModel):
    user_id: Optional[UUID] = None
    answers: List[SubmitAnswer]

class SubmissionOut(BaseModel):
    id: UUID
    score: float
    feedback: Optional[str] = None
    details: Any

class GenerateQuestionsRequest(BaseModel):
    source_text: str
    num_mcq: int = 3
    num_desc: int = 2
    num_code: int = 1
    topic: Optional[str] = None
    difficulty: Optional[str] = "medium"

class ReviewQuestionsOut(BaseModel):
    total: int
    sample: List[QuestionOut]

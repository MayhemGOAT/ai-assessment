from sqlalchemy import Column, Text, Integer, Float, JSON, ARRAY, TIMESTAMP, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from .database import Base

class Assessment(Base):
    __tablename__ = "assessments"
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(Text, nullable=False)
    created_by = Column(UUID(as_uuid=True), nullable=True)
    duration = Column(Integer, nullable=True)
    question_ids = Column(ARRAY(UUID(as_uuid=True)), nullable=True)
    status = Column(Text, nullable=False, server_default="draft")
    created_at = Column(TIMESTAMP, server_default=func.now())

class Question(Base):
    __tablename__ = "questions"
    id = Column(UUID(as_uuid=True), primary_key=True)
    type = Column(Text, nullable=False)
    question = Column(Text, nullable=False)
    options = Column(ARRAY(Text), nullable=True)
    correct_answer = Column(Text, nullable=True)
    explanation = Column(Text, nullable=True)
    topic = Column(Text, nullable=True)
    difficulty = Column(Text, nullable=True)
    source = Column(Text, nullable=True)
    auto_generated = Column(Text, nullable=False, server_default="true")

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), nullable=True)
    assessment_id = Column(UUID(as_uuid=True), ForeignKey("assessments.id"))
    submitted_at = Column(TIMESTAMP, server_default=func.now())
    score = Column(Float, nullable=True)
    feedback = Column(Text, nullable=True)
    details = Column(JSON, nullable=True)

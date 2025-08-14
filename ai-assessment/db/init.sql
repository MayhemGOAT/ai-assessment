CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS assessments (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  title TEXT NOT NULL,
  created_by UUID,
  duration INT,
  question_ids UUID[],
  status TEXT CHECK (status IN ('draft','published')) DEFAULT 'draft',
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS questions (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  type TEXT CHECK (type IN ('mcq','descriptive','coding')) NOT NULL,
  question TEXT NOT NULL,
  options TEXT[],
  correct_answer TEXT,
  explanation TEXT,
  topic TEXT,
  difficulty TEXT,
  source TEXT,
  auto_generated BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS submissions (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID,
  assessment_id UUID REFERENCES assessments(id),
  submitted_at TIMESTAMP DEFAULT NOW(),
  score FLOAT,
  feedback TEXT,
  details JSONB
);

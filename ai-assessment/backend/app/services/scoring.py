from typing import List, Dict, Any
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def score_assessment(questions: List[Dict[str, Any]], answers: List[Dict[str, Any]]):
    qmap = {str(q["id"]): q for q in questions}
    total = 0.0
    earned = 0.0
    details = []
    for ans in answers:
        q = qmap.get(str(ans["question_id"]))
        if not q: continue
        total += 1.0
        qtype = q["type"]
        correct = False
        if qtype == "mcq":
            correct = (str(ans["answer"]).strip() == str(q.get("correct_answer")).strip())
        elif qtype == "descriptive":
            ref = q.get("correct_answer") or ""
            student = str(ans["answer"] or "")
            if student.strip() == "":
                correct = False
            else:
                vec = TfidfVectorizer().fit_transform([ref, student])
                sim = cosine_similarity(vec[0:1], vec[1:2])[0][0]
                correct = sim >= 0.55
        elif qtype == "coding":
            ref = q.get("correct_answer") or ""
            student = str(ans["answer"] or "")
            tokens = ["def", "return", "for", "while", "if"]
            correct = (student.strip() == ref.strip()) or any(t in student for t in tokens)
        if correct: earned += 1.0
        details.append({"question_id": q["id"], "type": qtype, "correct": bool(correct), "expected": q.get("correct_answer"), "given": ans["answer"]})
    score = (earned / total * 100.0) if total else 0.0
    return score, details

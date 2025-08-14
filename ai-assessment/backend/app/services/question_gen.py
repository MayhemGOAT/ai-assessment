import random, re
from typing import List, Dict

def _sentences(text: str) -> List[str]:
    parts = re.split(r'[.!?]\s+', text)
    return [p.strip() for p in parts if len(p.strip()) > 20]

def generate_mcq(text: str, topic: str|None, difficulty: str, k: int) -> List[Dict]:
    sents = _sentences(text) or [text]
    out = []
    for i in range(k):
        base = random.choice(sents)
        correct = base[:50].strip()
        options = [correct, "Option X", "Option Y", "Option Z"]
        random.shuffle(options)
        out.append({
            "type": "mcq",
            "question": f"Which option best completes: '{base[:80]}...'?",
            "options": options,
            "correct_answer": correct,
            "explanation": "Derived from source sentence.",
            "topic": topic or "General",
            "difficulty": difficulty,
            "source": "ingested"
        })
    return out

def generate_desc(text: str, topic: str|None, difficulty: str, k: int) -> List[Dict]:
    sents = _sentences(text) or [text]
    out = []
    for i in range(k):
        base = random.choice(sents)
        out.append({
            "type": "descriptive",
            "question": f"Briefly explain the idea in: '{base[:100]}...'",
            "options": None,
            "correct_answer": base[:120],
            "explanation": "Free-form reference answer from source.",
            "topic": topic or "General",
            "difficulty": difficulty,
            "source": "ingested"
        })
    return out

def generate_code(text: str, topic: str|None, difficulty: str, k: int) -> List[Dict]:
    templates = [
        {
            "question": "Write a function `sum_array(arr)` that returns the sum of integers in arr.",
            "correct_answer": "def sum_array(arr):\n    return sum(arr)",
            "explanation": "Use Python's built-in sum."
        },
        {
            "question": "Given a string s, return True if it is a palindrome, ignoring case and spaces.",
            "correct_answer": "def is_palindrome(s):\n    t=''.join(s.lower().split())\n    return t==t[::-1]",
            "explanation": "Normalize then reverse compare."
        }
    ]
    out = []
    for i in range(k):
        tmpl = random.choice(templates)
        out.append({
            "type": "coding",
            "question": tmpl["question"],
            "options": None,
            "correct_answer": tmpl["correct_answer"],
            "explanation": tmpl["explanation"],
            "topic": topic or "Programming",
            "difficulty": difficulty,
            "source": "ingested"
        })
    return out

def generate_all(text: str, topic: str|None, difficulty: str, num_mcq: int, num_desc: int, num_code: int) -> List[Dict]:
    return (
        generate_mcq(text, topic, difficulty, num_mcq) +
        generate_desc(text, topic, difficulty, num_desc) +
        generate_code(text, topic, difficulty, num_code)
    )

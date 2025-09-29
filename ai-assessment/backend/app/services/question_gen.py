import json
from typing import List, Dict
from openai import OpenAI

# Initialize OpenAI client (requires OPENAI_API_KEY in your environment / .env file)
client = OpenAI()

def generate_all(topic: str, num_questions: int = 5) -> List[Dict[str, str]]:
    """
    Generate multiple-choice questions using OpenAI API.

    Args:
        topic (str): Subject or concept to generate questions about.
        num_questions (int): Number of questions to generate.

    Returns:
        List[Dict[str, str]]: A list of question objects.
    """

    prompt = f"""
    Generate {num_questions} multiple-choice questions on the topic "{topic}".
    Each question should have:
    - 'question' (string)
    - 'options' (list of 4 choices, strings)
    - 'answer' (the correct choice as string)

    Return the output as strict JSON list.
    Example:
    [
        {{
            "question": "What is 2+2?",
            "options": ["3","4","5","6"],
            "answer": "4"
        }}
    ]
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # you can switch to gpt-4o if needed
        messages=[
            {"role": "system", "content": "You are a helpful question generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    raw_content = response.choices[0].message.content.strip()

    try:
        results = json.loads(raw_content)
    except Exception:
        # If not valid JSON, wrap as fallback
        results = [{"question": "Error parsing AI output", "options": [], "answer": ""}]

    return results

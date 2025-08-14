def generate_feedback(details, questions):
    by_type = {"mcq": {"c":0,"t":0}, "descriptive":{"c":0,"t":0}, "coding":{"c":0,"t":0}}
    for d in details:
        if d["type"] in by_type:
            by_type[d["type"]]["t"] += 1
            by_type[d["type"]]["c"] += 1 if d["correct"] else 0
    parts = ["Automated feedback:"]
    for t, v in by_type.items():
        if v["t"]:
            pct = int(100*v["c"]/v["t"])
            parts.append(f"- {t.capitalize()}: {pct}% correct")
    parts.append("Review incorrect answers and explanations.")
    return "\n".join(parts)

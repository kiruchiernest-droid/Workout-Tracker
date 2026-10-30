def calculate_average(scores):
    valid = [s for s in scores if s is not None]
    if not valid:
        return None
    return round(sum(valid) / len(valid), 1)

def letter_grade(avg):
    if avg is None:
        return "N/A"
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Test
scores_a = [85, 90, 78]
scores_b = [72, None, 88]
scores_c = [60, None, None]

for s in [scores_a, scores_b, scores_c]:
    avg = calculate_average(s)
    print(f"Scores: {s} | Avg: {avg} | Grade: {letter_grade(avg)}")
student_scores = {
    "Hary": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

for key in student_scores:
    score = student_scores[key]
    if score > 90:
        print(f"{key}:Outstanding")
    elif score > 80:
        print(f"{key}:Exceed Exception")
    elif score > 70:
        print(f"{key}:Acceptable")   
def calculate_team_score(team):
    total = 0
    for student in team:
        total += sum(student.get("skills", {}).values())
    return total
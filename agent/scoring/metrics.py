def team_skill_score(team):
    return sum(sum(student["skills"].values()) for student in team)
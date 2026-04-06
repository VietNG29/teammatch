def score_student(student):
    return sum(student["skills"].values())

def create_balanced_teams(students, team_size):
    students = sorted(students, key=score_student, reverse=True)

    team_count = len(students) // team_size
    teams = [[] for _ in range(team_count)]

    for i, student in enumerate(students):
        teams[i % team_count].append(student)

    return teams

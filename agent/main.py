from matching_engine.assign import create_balanced_teams

students = [
    {"id": 1, "skills": {"python": 3, "frontend": 1}, "availability": ["mon", "wed"]},
    {"id": 2, "skills": {"python": 1, "frontend": 3}, "availability": ["wed", "fri"]},
    {"id": 3, "skills": {"python": 2, "frontend": 2}, "availability": ["mon", "fri"]},
    {"id": 4, "skills": {"python": 3, "frontend": 2}, "availability": ["wed", "fri"]},
]

teams = create_balanced_teams(students, 2)

print("Generated Teams:")
for i, team in enumerate(teams):
    print(f"Team {i+1}: {team}")
from fastapi import APIRouter
from app.simple_team_validator import validate_team_input
from app.simple_team_metrics import calculate_team_score
from app.simple_team_explainer import explain_team

router = APIRouter()

def score_student(student):
    skills = student.get("skills", {})
    return sum(skills.values())

def create_balanced_teams(students, team_size):
    students = sorted(students, key=score_student, reverse=True)

    team_count = len(students) // team_size
    if team_count == 0:
        return []

    teams = [[] for _ in range(team_count)]

    for i, student in enumerate(students[: team_count * team_size]):
        teams[i % team_count].append(student)

    return teams

@router.post("/generate-teams")
def generate_teams(payload: dict):
    course_id = payload.get("course_id")
    team_size = payload.get("team_size")
    students = payload.get("students")

    is_valid, message = validate_team_input(course_id, team_size, students)
    if not is_valid:
        return {
            "status": "error",
            "message": message
        }

    teams = create_balanced_teams(students, team_size)

    if not teams:
        return {
            "status": "error",
            "message": "Unable to generate teams with the provided input"
        }

    formatted_teams = []
    for idx, team in enumerate(teams, start=1):
        formatted_teams.append({
            "team_id": idx,
            "members": [member.get("name", f"Student-{member.get('id', idx)}") for member in team],
            "team_score": calculate_team_score(team),
            "explanation": explain_team(team)
        })

    return {
        "status": "success",
        "message": "Teams generated successfully",
        "course_id": course_id,
        "teams": formatted_teams
    }
def validate_team_input(course_id, team_size, students):
    if not course_id:
        return False, "course_id is required"

    if not isinstance(team_size, int) or team_size <= 0:
        return False, "team_size must be a positive integer"

    if not isinstance(students, list) or len(students) == 0:
        return False, "students must be a non-empty list"

    return True, "valid"
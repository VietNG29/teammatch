def summarize_team(team):
    ids = [s["id"] for s in team]
    return f"Team formed with students {ids} based on balanced skill distribution."
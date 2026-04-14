def explain_team(team):
    names = [member.get("name", "Unknown") for member in team]
    return f"This team was created to balance student skill distribution: {', '.join(names)}."
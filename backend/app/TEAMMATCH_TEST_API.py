import requests

url = "http://127.0.0.1:8000/api/generate-teams"

payload = {
    "course_id": "CS350",
    "team_size": 2,
    "students": [
        {
            "id": 1,
            "name": "Alice",
            "skills": {"python": 3, "frontend": 1},
            "availability": ["mon", "wed"]
        },
        {
            "id": 2,
            "name": "Bob",
            "skills": {"python": 1, "frontend": 3},
            "availability": ["wed", "fri"]
        },
        {
            "id": 3,
            "name": "Charlie",
            "skills": {"python": 2, "frontend": 2},
            "availability": ["mon", "fri"]
        },
        {
            "id": 4,
            "name": "Diana",
            "skills": {"python": 3, "frontend": 2},
            "availability": ["wed", "fri"]
        }
    ]
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
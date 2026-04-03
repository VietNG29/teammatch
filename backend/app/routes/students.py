from fastapi import APIRouter

router = APIRouter()

students = []

@router.get("/students")
def get_students():
    return students

@router.post("/students")
def add_student(student: dict):
    students.append(student)
    return {"message": "student added", "count": len(students)}

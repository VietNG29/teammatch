from fastapi import FastAPI
from app.routes import students

app = FastAPI(title="TeamMatch API")

app.include_router(students.router)

@app.get("/")
def root():
    return {"message": "TeamMatch API running"}

@app.get("/test")
def test():
    return {"status": "ok"}

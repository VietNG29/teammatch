from fastapi import FastAPI
from app.routes import students
from app.views import router as teammatch_router

app = FastAPI(title="TeamMatch API")

app.include_router(students.router)
app.include_router(teammatch_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "TeamMatch API running"}

@app.get("/test")
def test():
    return {"status": "ok"}
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,  
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    id :int
    name: str
    grade: int

students =[
    Student(id=1 , name="REHAMNIA Younes", grade=2),
    Student(id=2 , name="MEDJARI Mohamed", grade=7)
    ]

@app.get("/students/")
def read_students():
    return students

@app.post("/students/")
def create_students(New_student: Student):
    students.append(New_student)
    return New_student

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {"error": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message": "Student deleted"}
    return {"error":"Student not found"}

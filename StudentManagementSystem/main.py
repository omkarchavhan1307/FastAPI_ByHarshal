from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr
from pymongo import MongoClient
from typing import Dict, List
import json
import os


# ---------------------------------------------------
# FASTAPI APP
# ---------------------------------------------------

app = FastAPI(
    title="Student Management System",
    description="Student Management System using FastAPI, Pydantic, JSON and MongoDB",
    version="1.0"
)


# ---------------------------------------------------
# MONGODB CONNECTION
# ---------------------------------------------------

connectionString = MongoClient("mongodb://localhost:27017/")

database = connectionString["Student_Management"]

collection = database["Students"]


# ---------------------------------------------------
# JSON FILE
# ---------------------------------------------------

JSON_FILE = "students.json"


def read_json_students():

    if not os.path.exists(JSON_FILE):
        return []

    with open(JSON_FILE, "r") as file:
        return json.load(file)


def write_json_students(students):

    with open(JSON_FILE, "w") as file:
        json.dump(students, file, indent=4)


# ---------------------------------------------------
# PYDANTIC MODEL
# ---------------------------------------------------

class Student(BaseModel):

    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Student name"
    )

    roll: int = Field(
        ...,
        gt=0,
        description="Student roll number"
    )

    age: int = Field(
        ...,
        ge=16,
        le=60,
        description="Student age"
    )

    year: str = Field(
        ...,
        description="Academic year"
    )

    email: EmailStr

    subjects: Dict[str, int]

    hobbies: List[str]

    phone: str | None = None

    city: str | None = None


# ---------------------------------------------------
# ROOT API
# ---------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Welcome to Student Management System"
    }


# ---------------------------------------------------
# POST - ADD NEW STUDENT
# ---------------------------------------------------

@app.post("/student")
def add_student(student: Student):

    # Check duplicate roll number in MongoDB

    existing_student = collection.find_one({
        "roll": student.roll
    })

    if existing_student:

        raise HTTPException(
            status_code=400,
            detail="Student with this roll number already exists"
        )


    # Convert Pydantic object into dictionary

    student_data = student.model_dump()


    # -------------------------------
    # Store in MongoDB
    # -------------------------------

    collection.insert_one(student_data.copy())


    # -------------------------------
    # Store in JSON
    # -------------------------------

    students = read_json_students()

    students.append(student_data)

    write_json_students(students)


    return {
        "message": "Student added successfully",
        "student": student_data
    }


# ---------------------------------------------------
# GET - ALL STUDENTS
# ---------------------------------------------------

@app.get("/allstudents")
def get_all_students():

    students = list(
        collection.find(
            {},
            {
                "_id": 0
            }
        )
    )

    return {
        "count": len(students),
        "students": students
    }


# ---------------------------------------------------
# GET - FIND STUDENT BY NAME
# ---------------------------------------------------

@app.get("/student/name/{name}")
def find_student_by_name(name: str):

    student = collection.find_one(
        {
            "name": name
        },
        {
            "_id": 0
        }
    )

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "student": student
    }


# ---------------------------------------------------
# GET - FIND STUDENT BY ROLL
# ---------------------------------------------------

@app.get("/student/roll/{roll}")
def find_student_by_roll(roll: int):

    student = collection.find_one(
        {
            "roll": roll
        },
        {
            "_id": 0
        }
    )

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "student": student
    }
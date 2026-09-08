from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated
import json

app = FastAPI()


class StudentStruct(BaseModel):
    name: Annotated[str, Field(title="Enter your name")]
    roll: Annotated[int, Field(title="Enter your roll")]


@app.get("/")
def greet():
    return {"message": "student management system"}


@app.post("/register")
def Register(studentinfo: StudentStruct):

    sname = studentinfo.name
    sroll = studentinfo.roll

    sinfo = {
        "name": sname,
        "roll": sroll
    }

    with open("AllStudents.json", "r") as f:
        alldata = json.load(f)

    alldata.append(sinfo)

    with open("AllStudents.json", "w") as f2:
        json.dump(alldata, f2, indent=4)

    return {"message": "new student created"}
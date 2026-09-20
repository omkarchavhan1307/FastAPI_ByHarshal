from fastapi import FastAPI
from pydantic import BaseModel , Field
from typing import Annotated , Optional
import json

app = FastAPI()

class StudentStruct(BaseModel):
    name: Annotated[Optional[str],Field(title="enter new name",default=None)]
    age: Annotated[Optional[int],Field(title="enter new age",default=None)]
    email:Annotated[Optional[str],Field(title="enter new email",default=None)]


@app.get("/")
def greet():
    return {"message": "OmkarKomal's management system"}


@app.delete("/delete/{roll}")
def deleteStudent(roll: int, DeleteInfo : StudentStruct):

    with open("AllStudents.json", "r") as f:
        alldata = json.load(f)

    for i in alldata:
        if i["roll"] == roll:

            if DeleteInfo.roll == roll:
                alldata.remove(i)

            with open("AllStudents.json", "w") as f2:
                json.dump(alldata, f2)

            return {
                "message": "Student deleted successfully",
                "student": i
            }

    return {
        "message": "Student not found"
    }
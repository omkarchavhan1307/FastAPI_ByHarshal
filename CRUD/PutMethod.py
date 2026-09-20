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
    return {"message" : "Omkar's Management System"}

@app.put("/edit/{roll}")
def Update_Student(roll : int, UpdateInfo:StudentStruct):
    with open("AllStudents.json","r") as f:
        alldata = json.load(f)

    for i in alldata:
        if i["roll"] == roll:
            if UpdateInfo.name != None:
                i["name"] = UpdateInfo.name

            if UpdateInfo.age != None:
                i["age"] = UpdateInfo.age

            if UpdateInfo.email != None:
                i["email"] = UpdateInfo.email

    with open("AllStudents.json","w") as f2:
        json.dump(alldata , f2)

    return{"message" : "Student Updated."}

from fastapi import FastAPI
import json


app = FastAPI()



@app.get("/")
def greet():
    return {"message":"hello"}


@app.get("/allstudents")
def AllStudent():
    with open("AllStudents.json","r") as f:
        alldata = json.load(f)

        return alldata


@app.get("/allstudents/{name}")
def AllStudent(name):
    with open("AllStudents.json","r") as f:
        alldata = json.load(f)

    for i in alldata:
        if i["name"] == name:
            return i

    return {"message":"user not found"}

        
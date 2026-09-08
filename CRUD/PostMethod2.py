from fastapi import FastAPI
from pydantic import BaseModel , Field
from typing import Annotated
from pymongo import MongoClient

connectionString = MongoClient("mongodb://localhost:27017/")

database = connectionString["studentdb001"]

collection = database["allstudents"]

app = FastAPI()

class studstruct(BaseModel):
    name:Annotated[str,Field(title="enter your name")]
    roll:Annotated[int,Field(title="enter your roll")]


@app.get("/")
def greet():
    return {"message":"student management system"}


@app.post("/newstudent")
def newStudent(info:studstruct):
    sname = info.name
    sroll = info.roll

    sinfo = {
        "name":sname,
        "roll":sroll
    }

    collection.insert_one(sinfo)

    return{"message" : "new student store in mongodb"}
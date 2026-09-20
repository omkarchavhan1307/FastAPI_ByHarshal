from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel , Field
from typing import Annotated , Optional

connectionstring = MongoClient("mongodb://localhost:27017/")

database = connectionstring["studentdb001"]

collectionname = database["allstudents"]



app = FastAPI()

class StudentStruct(BaseModel):
    name: Annotated[Optional[str],Field(title="enter new name",default=None)]
    age: Annotated[Optional[int],Field(title="enter new age",default=None)]
    email:Annotated[Optional[str],Field(title="enter new email",default=None)]

@app.get("/")
def greet():
    return{"message": "OmkarKomal's management system"}


@app.put("/edit/{roll}")
def Student_Update(roll : int, UpdateInfo:StudentStruct):

    alldata = list(collectionname.find({}, {"_id" : 0}))

    for i in alldata:
        if i["roll"] == roll:
            if UpdateInfo.name != None:
                i["name"] = UpdateInfo.name
        
            if UpdateInfo.age != None:
                i["age"] = UpdateInfo.age
        
            if UpdateInfo.email != None:
                i["email"] = UpdateInfo.email 

        collectionname.insert_one(roll)

    return{"message" : "Student Updated"}


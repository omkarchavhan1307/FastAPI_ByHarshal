from fastapi import FastAPI
from pymongo import MongoClient

connectionstring = MongoClient("mongodb://localhost:27017/")

database = connectionstring["studentdb001"]

collectionname = database["allstudents"]



app = FastAPI()



@app.get("/")
def greet():
    return{"message": "management system"}

@app.get("/allstudents")
def Allstudents():

    alldata = list(collectionname.find({},{"name":1,"roll":1,"_id":0}))

    return alldata


@app.get("/allstudents/{name}")
def findstudentbyname(name):
    allinfo = list(collectionname.find({},{"name":1,"roll":1,"_id":0}))

    for i in allinfo:
        if i["name"]== name:
            return i

    return {"message":"user not found"}
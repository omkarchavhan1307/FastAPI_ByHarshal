from fastapi import APIRouter
from Model.studentmodel import StudentStruct
from Model.studentupdate import updateStruct
from Database.dbconnection import collectionName

router = APIRouter()


@router.post("/student")
def CreateStudent(student: StudentStruct):
    try:
        sinfo = {
            "roll": student.roll,
            "name": student.name,
            "age": student.age,
            "email": student.email
        }

        collectionName.insert_one(sinfo)

        return {"message": "new student created"}

    except Exception as e:
        print("ERROR:", e)
        return {"message": "Something wrong", "error": str(e)}



@router.get("/studentslist")
def Getallstudents():
    try:
        alldata = list(collectionName.find({}, {"_id": 0}))
        return alldata

    except:
        return "something wrong"


@router.put("/edit/{roll}")
def UpdateStudent(roll:int,studentinfo:updateStruct):
    try:
        alldata = list(collectionName.find({},{"_id":0}))
        updatedinfo = {}


        for i in alldata:
            if i["roll"]==roll:

                if studentinfo.name != None:
                    updatedinfo["name"]=studentinfo.name

                if studentinfo.age != None:
                    updatedinfo["age"]=studentinfo.age

                if studentinfo.email != None:
                    updatedinfo["email"]=studentinfo.email

                collectionName.update_one(
                    {"roll":roll},
                    {"$set":updatedinfo}
                )

                return {"message":"user updated"}    
    except:
        return{"message":"something wrong"}


@router.delete("/delet/{roll}")
def Deletstudent(roll:int):

    try:
        alldata = list(collectionName.find({},{"_id":0}))
        for i in alldata:
            if i["roll"]==roll:
                collectionName.delete_one({"roll":roll})
                return{"message":"student deleted"}
    except:
        return {"message":"something wrong"}
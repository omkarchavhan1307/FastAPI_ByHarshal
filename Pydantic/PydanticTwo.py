from pydantic import BaseModel

name = "DemoUser"
age = 10

studentInfo = {
    "name":name,
    "age":age
}

class UserStructure(BaseModel):
    name:str
    age:int

userObj = UserStructure(name=studentInfo["name"],age=studentInfo["age"])

usersList = []

def VoatingSystem(userObj):
    print(userObj.name,userObj.age)
    # print()
    usersList.append(userObj)
    print("data store in database")


VoatingSystem(userObj)
print(usersList)

def EligibleUsers():
    for i in usersList:
        if i.age>18:
            print("eligible for voating")
        else:
            print("not eligible for voating")

EligibleUsers()
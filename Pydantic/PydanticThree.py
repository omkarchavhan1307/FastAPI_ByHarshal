from pydantic import BaseModel , EmailStr , HttpUrl , Field


name = "DemoUser"
age = 50
mail = "demouser@gmail.com"
hobbies = ["playing","reading"]
linkdin = "https://demouser.com"

studentInfo = {
    "name":name,
    "age":age,
    "mail":mail,
    "hobbies":hobbies,
    "linkdin":linkdin
}

class UserStructure(BaseModel):
    name:str = Field(min_length=5 , title="Enter Your Name" , description="length should be less than 10",examples="DemoUser" , default="Null")
    age:int = Field(gt=18, lt=90)
    mail:EmailStr
    hobbies: list
    linkdin:HttpUrl


userObj = UserStructure(name=studentInfo["name"],age=studentInfo["age"],mail=studentInfo["mail"],hobbies=studentInfo["hobbies"],linkdin=studentInfo["linkdin"])


def VoatingSystem(userObj):
    print(userObj.name)
    print(userObj.age)
    print(userObj.mail)
    print(userObj.hobbies)
    print(userObj.linkdin)
    print("data store in database")


VoatingSystem(userObj)
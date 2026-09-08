from pydantic import BaseModel , EmailStr , HttpUrl , Field
from typing import List , Optional , Annotated


name = "DemoUser"
age = "50"
mail = "demouser@gmail.com"
hobbies = ["playing","reading"]
linkdin = "https://demouser.com"
# phonenumber = 8888888888

studentInfo = {
    "name":name,
    "age":age,
    "mail":mail,
    "hobbies":hobbies,
    "linkdin":linkdin,
    # "phonenumber":phonenumber
}

class UserStructure(BaseModel):
    name: Annotated[str, Field(min_length=5 , title="Enter Your Name" , description="length should be less than 10",examples="DemoUser" , default="Null")]
    age: Annotated [int , Field(gt=18, lt=90)]
    mail:Optional[Annotated[EmailStr , Field(title="Enter Email")]]  = None
    hobbies: Annotated[List[str], Field(title="Enter hobbies")]
    linkdin: Annotated[HttpUrl , Field(title="Enter Proper url")]
    # phonenumber:Annotated[int , Field(min_length=10)]


# userObj = UserStructure(name=studentInfo["name"],age=studentInfo["age"],mail=studentInfo["mail"],hobbies=studentInfo["hobbies"],linkdin=studentInfo["linkdin"],phonenumber=studentInfo["phonenumber"])
userObj = UserStructure(**studentInfo)

def VoatingSystem(userObj):
    print(userObj.name)
    print(userObj.age)
    print(userObj.mail)
    print(userObj.hobbies)
    print(userObj.linkdin)
    # print(userObj.phonenumber)
    print("data store in database")


VoatingSystem(userObj)
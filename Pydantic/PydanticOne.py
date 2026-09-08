name = "DemoUser"
age = "twenty"

studentInfo = {
    "name":name,
    "age":age
}

usersList = []

def VoatingSystem(studentInfo):
    print(studentInfo["name"],studentInfo["age"])
    # print()
    usersList.append(studentInfo)
    print("data store in database")


VoatingSystem(studentInfo)
print(usersList)

def EligiveUser():
    for i in usersList:
        if type(i["age"])==int:

            if i["age"] > 18:
                print("eligible for voating")
            else:
                print("not eligible for voating")
        else:
            print("incorect data type")
EligiveUser()
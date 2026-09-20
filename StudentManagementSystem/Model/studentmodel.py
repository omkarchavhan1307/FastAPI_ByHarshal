from pydantic import BaseModel , Field , EmailStr
from typing import Annotated 

class StudentStruct(BaseModel):
    roll: Annotated[int,Field(title="Enter your rollno")]
    name: Annotated[str,Field(title="Enter your Name")]
    age: Annotated[int,Field(title="Enter your age")]
    email: Annotated[EmailStr,Field(title="Enter your email")]
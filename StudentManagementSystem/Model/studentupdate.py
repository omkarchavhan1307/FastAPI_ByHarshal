from pydantic import BaseModel , Field , EmailStr
from typing import Annotated , Optional

class updateStruct(BaseModel):
    name: Annotated[Optional[str],Field(title="Enter your rollno",default=None)]
    age: Annotated[Optional[int],Field(title="Enter your rollno",default=None)]
    email: Annotated[Optional[EmailStr],Field(title="Enter your rollno",default=None)]
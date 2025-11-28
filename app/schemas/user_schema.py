from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    name: str

class UserResponse(UserCreate):
    id: int
    model_config = {"from_attributes": True}

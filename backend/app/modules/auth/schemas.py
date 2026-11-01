from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    email: str
    name: str
    role: str
    model_config = {"from_attributes": True}


class LoginResult(BaseModel):  # frontend ki features/auth/api.ts se match karein
    token: str
    user: UserOut

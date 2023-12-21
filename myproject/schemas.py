from pydantic import BaseModel



class ForecastCreate(BaseModel):
    city: str
    date: str
    description: str
    temperature_high: float
    temperature_low: float

class Forecast(ForecastCreate):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class LocationBase(BaseModel):
    city: str
    country: str

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True
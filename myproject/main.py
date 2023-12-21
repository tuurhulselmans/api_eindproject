from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import authenticate_user, create_access_token
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import crud
import auth

import models
import schemas
from database import SessionLocal, engine
import os



if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
allowed_origin = "https://dancing-melba-034ff1.netlify.app"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[allowed_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.post("/forecast/", response_model=schemas.Forecast)
def create_forecast(forecast: schemas.ForecastCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    # Only authenticated users can add forecasts
    return crud.create_forecast(db=db, forecast=forecast)

@app.get("/forecast/", response_model=list[schemas.Forecast])
def read_forecasts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # All authenticated users can access forecast data
    return crud.get_forecasts(db, skip=skip, limit=limit)

@app.get("/forecast/{forecast_id}", response_model=schemas.Forecast)
def read_forecast(forecast_id: int, db: Session = Depends(get_db)):
    db_forecast = crud.get_forecast(db, forecast_id)
    if db_forecast is None:
        raise HTTPException(status_code=404, detail="Forecast not found")
    return db_forecast


@app.get("/forecast_ordered/{city}", response_model=list[schemas.Forecast])
def get_forecast_by_city_ordered_with_temp(
        city: str,
        min_temp: float = None,  # Default value is None
        max_temp: float = None,  # Default value is None
        db: Session = Depends(get_db)
):
    # Get the forecast data for the specified city and order by date
    forecast = crud.get_forecast_by_city_ordered(db, city)

    # Filter forecast data based on min_temp and max_temp if provided
    filtered_forecast = []
    for item in forecast:
        if (min_temp is None or item.temperature_low >= min_temp) and \
                (max_temp is None or item.temperature_high <= max_temp):
            filtered_forecast.append(item)

    if not filtered_forecast:
        raise HTTPException(status_code=404, detail="Forecast data not found for the specified criteria")

    return filtered_forecast

@app.delete("/forecast/{forecast_id}", response_model=schemas.Forecast)
def delete_forecast(forecast_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_forecast = crud.get_forecast(db, forecast_id)
    if db_forecast is None:
        raise HTTPException(status_code=404, detail="Forecast not found")
    db.delete(db_forecast)
    db.commit()
    return db_forecast

@app.put("/forecast/{forecast_id}", response_model=schemas.Forecast)
def update_forecast(forecast_id: int, forecast: schemas.ForecastCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_forecast = crud.get_forecast(db, forecast_id)
    if db_forecast is None:
        raise HTTPException(status_code=404, detail="Forecast not found")
    for key, value in forecast.dict().items():
        setattr(db_forecast, key, value)
    db.commit()
    db.refresh(db_forecast)
    return db_forecast


@app.post("/locations/", response_model=schemas.Location)
def create_location(location: schemas.LocationCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.create_location(db=db, location=location)

@app.get("/locations/{location_id}", response_model=schemas.Location)
def read_location(location_id: int, db: Session = Depends(get_db)):
    db_location = crud.get_location(db, location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}



@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user



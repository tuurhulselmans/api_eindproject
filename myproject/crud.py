from sqlalchemy.orm import Session

import auth
from models import Forecast
import models
import schemas
from typing import Optional

def create_forecast(db: Session, forecast: schemas.ForecastCreate):
    db_forecast = Forecast(**forecast.dict())
    db.add(db_forecast)
    db.commit()
    db.refresh(db_forecast)
    return db_forecast

def get_forecasts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Forecast).offset(skip).limit(limit).all()

def get_forecast(db: Session, forecast_id: int):
    return db.query(Forecast).filter(Forecast.id == forecast_id).first()

def get_weather_by_city(db: Session, city: str):
    return db.query(Weather).filter(Weather.city == city).first()

def get_forecast_by_city_ordered(db: Session, city: str):
    return db.query(Forecast).filter(Forecast.city == city).order_by(Forecast.date).all()

# CRUD operations for User


# CRUD operations for Location
def create_location(db: Session, location: schemas.LocationCreate):
    db_location = models.Location(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

def get_location(db: Session, location_id: int):
    return db.query(models.Location).filter(models.Location.id == location_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
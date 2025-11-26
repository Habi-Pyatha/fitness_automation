from sqlalchemy import Column, Integer, String, Float, JSON, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
import datetime

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, autoincrement=True)
  email = Column(String,unique=True)
  timezone = Column(String, default='UTC')
  created_at = Column(DateTime, default=datetime.datetime.utcnow)

class WorkoutLog(Base):
  __tablename__ = "workout_logs"
  id = Column(Integer, primary_key=True, autoincrement=True)
  user_id = Column(Integer, ForeignKey('users.id')) 
  raw_text = Column(String)
  parsed = Column(JSON)
  created_at = Column(DateTime, default=datetime.datetime.utcnow)

class WorkoutPlan(Base):
  __tablename__ = "workout_plans"
  id = Column(Integer, primary_key=True, autoincrement=True)
  user_id = Column(Integer, ForeignKey('users.id')) 
  weeks_start = Column(DateTime
  plan_json = Column(JSON)
  generated_at = Column(DateTime, default=datetime.datetime.utcnow)
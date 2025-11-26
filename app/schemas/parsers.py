from pydantic import BaseModel 
from typing import List, Optional

class Exercise(BaseModel):
  name:str
  sets: int
  reps: List[int]
  weight: Optional[str]
  muscle_group: Optional[str]

class ParsedWorkout(BaseModel):
  date: Optional[str]
  exercises: List[Exercise]
  notes: Optional[str]
  
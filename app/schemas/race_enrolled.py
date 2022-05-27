from uuid import UUID
from pydantic import BaseModel
from typing import Optional
from models.race_enrolled import RaceEnum

class RaceEnrolledBase(BaseModel):
    category_id: Optional[UUID]
    school_id: Optional[UUID]
    race: RaceEnum
    percent: Optional[str]
    count: Optional[str]
    
    
class RaceEnrolledInDB(RaceEnrolledBase):
    id: UUID
    

class RaceEnrolledInResp(RaceEnrolledInDB):
    pass
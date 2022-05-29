from uuid import UUID
from pydantic import BaseModel
from typing import List, Optional
from models.race_enrolled import RaceEnum

class RaceEnrolledBase(BaseModel):
    category_id: Optional[UUID]
    school_id: Optional[UUID]
    race: RaceEnum
    percent: Optional[str]
    count: Optional[float]
    
    
class RaceEnrolledInDB(RaceEnrolledBase):
    id: UUID
    

class RaceEnrolledInResp(RaceEnrolledInDB):
    pass


class RaceEnrollmentsInResp(BaseModel):
    chart_id: Optional[int]
    race_enrollments: List[RaceEnrolledInResp]
    total_count: int

from uuid import UUID
from pydantic import BaseModel
from typing import List, Optional
from models.gender_enrolled import GenderEnum

class GenderEnrolledBase(BaseModel):
    category_id: Optional[UUID]
    school_id: Optional[UUID]
    gender: GenderEnum
    percent: Optional[str]
    count: Optional[int]
    
    
class GenderEnrolledInDB(GenderEnrolledBase):
    id: UUID
    

class GenderEnrolledInResp(GenderEnrolledInDB):
    pass


class GenderEnrollmentsInResp(BaseModel):
    chart_id: Optional[UUID]
    gender_enrollments: List[GenderEnrolledInResp]
    total_count: int
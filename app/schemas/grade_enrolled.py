from uuid import UUID
from pydantic import BaseModel
from typing import List, Optional
from models.grade_enrolled import GradeEnum

class GradeEnrolledBase(BaseModel):
    category_id: Optional[UUID]
    school_id: Optional[UUID]
    grade: GradeEnum
    count: Optional[float]
    
    
class GradeEnrolledInDB(GradeEnrolledBase):
    id: UUID
    

class GradeEnrolledInResp(GradeEnrolledInDB):
    pass


class GradeEnrollmentsInResp(BaseModel):
    chart_id: Optional[int]
    grade_enrollments: List[GradeEnrolledInResp]
    total_count: int
from uuid import UUID
from pydantic import BaseModel
from typing import Optional
from models.grade_enrolled import GradeEnum

class GradeEnrolledBase(BaseModel):
    category_id: Optional[UUID]
    school_id: Optional[UUID]
    grade: GradeEnum
    count: Optional[str]
    
    
class GradeEnrolledInDB(GradeEnrolledBase):
    id: UUID
    

class GradeEnrolledInResp(GradeEnrolledInDB):
    pass
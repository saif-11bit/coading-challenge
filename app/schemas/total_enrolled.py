from uuid import UUID
from pydantic import BaseModel
from typing import Optional, List


class TotalEnrolledBase(BaseModel):
    category_id: Optional[UUID]
    school_id: Optional[UUID]
    count: Optional[float]
    
    
class TotalEnrolledInDB(TotalEnrolledBase):
    id: UUID
    

class TotalEnrolledInResp(TotalEnrolledInDB):
    pass


class TotalEnrollmentsInResp(BaseModel):
    total_enrollments: List[TotalEnrolledInResp]
    total_count: int
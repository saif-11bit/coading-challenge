from uuid import UUID
from pydantic import BaseModel
from typing import Optional


class TotalEnrolledBase(BaseModel):
    category_id: Optional[UUID]
    school_id: Optional[UUID]
    count: Optional[str]
    
    
class TotalEnrolledInDB(TotalEnrolledBase):
    id: UUID
    

class TotalEnrolledInResp(TotalEnrolledInDB):
    pass
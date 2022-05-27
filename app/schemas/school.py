from uuid import UUID
from pydantic import BaseModel
from typing import Optional, List


class SchoolBase(BaseModel):
    DBN: Optional[str]
    school_name: Optional[str]
    

class SchoolInDB(SchoolBase):
    id: UUID    


class SchoolInResp(SchoolInDB):
    pass


class SchoolCreation(SchoolBase):
    pass

class SchoolsInResp(BaseModel):
    schools: List[SchoolInResp]
    total_count: int

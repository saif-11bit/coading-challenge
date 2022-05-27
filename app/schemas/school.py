from uuid import UUID
from pydantic import BaseModel
from typing import Optional


class SchoolBase(BaseModel):
    DBN: Optional[str]
    school_name: Optional[str]
    

class SchoolInDB(SchoolBase):
    id: UUID    


class SchoolInResp(SchoolInDB):
    pass

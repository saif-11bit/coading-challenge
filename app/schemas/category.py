from uuid import UUID
from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    category_name: Optional[str]
    

class CategoryInDB(CategoryBase):
    id: UUID
    

class CategoryInResp(CategoryInDB):
    pass
from pydantic import BaseModel
from typing import Optional, List



class TicketsBase(BaseModel):
	subject: str
	description : Optional[str] = None


class TicketsShow(BaseModel):
	subject: str
	description : str

	class Config:
		orm_mode = True


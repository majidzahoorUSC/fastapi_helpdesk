from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from ..crud import helpdesk
from ..utils import database
from ..schemas import schemas

get_db = database.get_db


router = APIRouter(
	prefix="/ticket",
	tags=["Helpdesk"]
	)

@router.get('/', response_model=List[schemas.TicketsShow])
def all(db:Session = Depends(get_db)):
	return helpdesk.get_all(db)

@router.post('/')
def create(request: schemas.TicketsBase, db: Session = Depends(get_db)):
	return helpdesk.create(request, db)

@router.get('/{id}',response_model=schemas.TicketsShow)
def show(id: int, db:Session = Depends(get_db)):
	return helpdesk.show(id, db)
@router.put('/{id}')
def update(id: int, request: schemas.TicketsBase, db: Session = Depends(get_db)):
	return helpdesk.update(id, request, db)

@router.delete('/{id}')
def destroy(id: int, db: Session = Depends(get_db)):
	return helpdesk.destroy(id, db)
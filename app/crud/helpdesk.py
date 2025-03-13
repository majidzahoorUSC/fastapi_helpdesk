from sqlalchemy.orm import Session
from fastapi import status, HTTPException, Depends
from ..models import models
from ..schemas import  schemas


def get_all(db: Session):
    tickets = db.query(models.Tickets).all()
    if not tickets:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No tickets found")
    return tickets

def create(request, db: Session):
    new_ticket = models.Tickets(subject=request.subject, description= request.description, user_id=1)
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

def show(id: int, db=Session):
    ticket = db.query(models.Tickets).filter(models.Tickets.id == id).first()
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Ticket with the id {id} not found")
    return ticket

def update(id: int, request: schemas.TicketsBase , db: Session):
    ticket = db.query(models.Tickets).filter(models.Tickets.id == id).first()
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Ticket with the id {id} not found")
    ticket.subject = request.subject
    ticket.description= request.description
    db.commit()
    db.refresh(ticket)
    return {"msg" : f'Successfully update ticket id {id}'}

def destroy(id: int, db: Session):
    ticket = db.query(models.Tickets).filter(models.Tickets.id == id).first()
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Ticket with the id {id} not found")
    db.delete(ticket)
    db.commit()
    return {"msg" : "Ticket with id {id} has been deleted successfully"}
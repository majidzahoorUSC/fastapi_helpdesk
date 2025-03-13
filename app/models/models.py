from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship
from ..utils.database import Base


class Team(Base):
    __tablename__= 'team'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)


class Tickets(Base):
    __tablename__= 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, index=True)
    description = Column(String)
    date = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))  # Updated line
    helpdesk_team = Column(Integer, ForeignKey("team.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    assignedTo = relationship("Users", back_populates="tickets")


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    tickets = relationship('Tickets', back_populates="assignedTo")

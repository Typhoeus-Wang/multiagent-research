from sqlalchemy import Column, Integer, String
from .database import Base

# based off the standard:
#   https://github.com/nostr-protocol/nips/blob/master/01.md
class Event(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key=True, index=True)
    kind = Column(Integer)       # 0
    tags = Column(String)        # study tags (eg. 0.3-1--1)
    pubkey = Column(String)      # participant id
    created_at = Column(Integer) # unix time
    content = Column(String)     # json data
    


# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")

from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base
from db.models.logo import Logo

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    logos = relationship("Logo", back_populates="creator")
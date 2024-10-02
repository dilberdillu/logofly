from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship

from db.base_class import Base


class Logo(Base):
    id = Column(Integer, primary_key=True)
    prompt = Column(Text, nullable=False)
    image = Column(LargeBinary, nullable=False)
    creator_id = Column(Integer, ForeignKey("user.id"))
    creator = relationship("User", back_populates="logos")
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=True)


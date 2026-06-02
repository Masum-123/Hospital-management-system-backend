import uuid
from sqlalchemy import Column, String, JSON
from app.db.base import Base
class Disease(Base):
    __tablename__ = "diseases"
    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True
    )
    disease_name = Column(String, nullable=False)
    specialized_doctor_id = Column(JSON)
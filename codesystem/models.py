from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base

class CodeSystemConcept(Base):
    __tablename__ = 'codesystem_concept'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    display = Column(String, nullable=True)
    definition = Column(String, nullable=True)
    codesystem_id = Column(Integer, index=True)

class CodeSystem(Base):
    __tablename__ = 'codesystem'

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    version = Column(String, nullable=True)
    name = Column(String)
    status = Column(String, default="active")
    description = Column(String, nullable=True)

    concepts = relationship("CodeSystemConcept", back_populates="codesystem")

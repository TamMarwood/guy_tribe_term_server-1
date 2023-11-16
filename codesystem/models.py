from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base
from core.util import DbModelToDictMixin

class CodeSystemConcept(DbModelToDictMixin,Base):
    __tablename__ = 'concept'

    # id = Column(Integer, primary_key=True, index=True)
    code = Column(String, primary_key=True, index=True)
    # code = Column(String, index=True)
    display = Column(String, nullable=True)
    name = Column(String, nullable = True)
    definition = Column(String, nullable=True)

class ConceptRelationship(Base):
    __tablename__ = 'concept_relationship'
    
    # id = Column(Integer, primary_key=True, index=True)
    code = Column(String, primary_key=True, index=True)
    # code = Column(String, index=True)
    display = Column(String, nullable=True)
    definition = Column(String, nullable=True)
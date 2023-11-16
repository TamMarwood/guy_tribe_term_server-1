from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base
from core.util import DbModelToDictMixin

class Concept(DbModelToDictMixin,Base):
    __tablename__ = 'concept'

    concept_id = Column(Integer, primary_key=True, index=True)
    concept_name = Column(String, primary_key=True, index=True)
    domain_id = Column(String, nullable=True)
    vocabulary_id = Column(String, nullable = True)
    concept_class_id = Column(String, nullable=True)
    standard_concept = Column(String, nullable=True)
    concept_code = Column(String, nullable=True)
    valid_start_date = Column(String, nullable=True)
    valid_end_date = Column(String, nullable=True)

class ConceptRelationship(DbModelToDictMixin,Base):
    __tablename__ = 'concept_relationship'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    concept_id_1 = Column(String)
    concept_id_2 = Column(String)
    relationship_type = Column(String)
from typing import List, Optional
from pydantic import BaseModel

class ConceptBase(BaseModel):
    concept_id: int
    concept_name: Optional[str]
    domain_id: Optional[str]
    vocabulary_id: Optional[str]
    concept_class_id: Optional[str]
    standard_concept: Optional[str]
    concept_code: Optional[str]
    valid_start_date: Optional[str]
    valid_end_date: Optional[str]    

class Concept(ConceptBase):
    class Config:
        orm_mode = True

class ConceptRelationshipBase(BaseModel):
    concept_id_1: int
    concept_id_2: int
    relationship: str

class ConceptRelationship(ConceptBase):
    class Config:
        orm_mode = True

class CodeSystemBase(BaseModel):
    resourceType: str = "CodeSystem"
    url: str
    version: Optional[str] = None
    name: str
    status: str = "active"
    description: Optional[str] = None
    concept: List[ConceptBase]

    class Config:
        schema_extra = {
            "example": {
                "resourceType": "CodeSystem",
                "url": "http://example.org/CodeSystem/mycodesystem",
                "version": "1.0",
                "name": "MyCodeSystem",
                "status": "active",
                "description": "Example CodeSystem for demonstration purposes",
                "concept": [
                    {
                        "code": "12345",
                        "display": "Diabetes",
                        "definition": "A group of metabolic diseases characterized by high blood sugar levels"
                    },
                    {
                        "code": "67890",
                        "display": "Hypertension",
                        "definition": "High blood pressure, a long-term medical condition"
                    },
                    {
                        "code": "54321",
                        "display": "Hyperlipidemia",
                        "definition": "Elevated levels of lipids (fats) in the blood"
                    }
                ]
            }
        }

class CodeSystem(CodeSystemBase):
    id: int
    class Config:
        orm_mode = True



# class CodeSystem(Base):
#     __tablename__ = 'codesystem'

#     id = Column(Integer, primary_key=True, index=True)
#     url = Column(String, index=True)
#     version = Column(String, nullable=True)
#     name = Column(String)
#     status = Column(String, default="active")
#     description = Column(String, nullable=True)

#     concepts = relationship("CodeSystemConcept", back_populates="codesystem")

from typing import List, Optional
from pydantic import BaseModel

class CodeSystemConcept(BaseModel):
    code: str
    display: Optional[str]
    definition: Optional[str]

class CodeSystem(BaseModel):
    resourceType: str = "CodeSystem"
    url: str
    version: Optional[str] = None
    name: str
    status: str = "active"
    description: Optional[str] = None
    concept: List[CodeSystemConcept]

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

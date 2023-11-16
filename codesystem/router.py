from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

from .schemas import CodeSystemBase, CodeSystemConceptBase, CodeSystemConcept
from .services import CodeSystemService, CodeSystemConceptsService
from core.database import get_db

router = APIRouter()

# @router.get("/", response_model=List[Item])
# @router.get("/")
# async def read_items(code_system_service: CodeSystemService = Depends()):
#     return code_system_service.get_items()

@router.get("/", response_model=CodeSystemBase)
async def root(concept_service: CodeSystemConceptsService = Depends()):
    response = CodeSystemBase(**CodeSystemBase.Config.schema_extra["example"])
    concepts = concept_service.get_concepts()
    concepts_base = [CodeSystemConceptBase(**concept.dict()) for concept in concepts]
    response.concept = concepts_base
    return response

@router.get("/concepts", response_model=list[CodeSystemConcept])
async def concepts(concept_service: CodeSystemConceptsService = Depends()):
    concepts = concept_service.get_concepts()
    return concepts
@router.get("/concepts/create")
async def concepts_create(concept_service: CodeSystemConceptsService = Depends()):
    import csv
    from pathlib import Path
    csv_path = Path('data/concepts.csv')
    concepts: list[CodeSystemConcept] = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            concept = CodeSystemConceptBase(**row)
            codeSystemConcept = concept_service.create_concept(concept)
            if codeSystemConcept:
                concepts.append(codeSystemConcept)
    return concepts

@router.get("/$subsumes")
async def subsumes(URL: [base]/CodeSystem/$subsumescodeA=['concept_id1']&codeB=['concept_id2']):
    subsume_relationship(codeA,codeB):
        for i in relationship_table.iterrows:
            if codeA = relationship_table['concept_id1'] & codeB = relationship_table['concept_id2']:
                relationship = relationship_table['relationship_id']
                return relationship_table['relationship_id']
            else:
                relationship = 'There is an error. Subsumption cannot be tested'
    return print('this is subsumes response',relationship)

@router.get("/$validate-code")
def validate_code(url: str, codeSystem, code: str, version: str, display, coding: str, codeableConcept, date: str, abstract, displayLanguage: str):
    return { "Response" : "this is a validate code response"}

@router.get("/{id}/$validate-code")
async def validate_code(id):
    return { "Response" : "this is a validate code response for id %s" % id}

@router.get("/$lookup")
def look_up(code: str | None = None, uri: str | None = None , version: str | None = None, coding: str | None = None, date: str  | None = None, displayLanguage: str | None = None, concept_service: CodeSystemConceptsService = Depends()):
    code_system_concept = concept_service.get_concept_by_code(code)
    
    return {
        "resourceType" : "Parameters",
        "parameter": [
            {
                "name" : "name",
                "valueString": code_system_concept.name
            },
            {
                "name": "version",
                "valueString": version
            },
            {
                "name": "display",
                "valueString": code_system_concept.display
            },
            {
                "name": "definition",
                "valueString": code_system_concept.definition
            },
            {
                "name": "designation",
                "part": [
                    {
                        "name": "value",
                        "valueString": "Test"
                    }
                ]
            },
            {
                "name": "property",
                "part": [
                    {
                        "name": "code",
                        "valueString": "property_name"
                    },
                    {
                        "name": "value",
                        "valueString": "value"
                    },
                    {
                        "name": "description",
                        "valueString": "description"
                    }
                ]
            }
        ]
    }

@router.get("/$validate")
async def validate():
    return { "Response" : "this is a validate response"}



# @router.get("/{item_id}", response_model=Item)
# async def read_item(item_id: int, item_service: ItemService = Depends()):
#     return item_service.get_item(item_id)

# @router.put("/{item_id}", response_model=Item)
# async def update_item(item_id: int, item: ItemUpdate, item_service: ItemService = Depends()):
#     return item_service.update_item(item_id, item)

# @router.delete("/{item_id}", response_model=Item)
# async def delete_item(item_id: int, item_service: ItemService = Depends()):
#     return item_service.delete_item(item_id)

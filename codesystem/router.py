from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

from .schemas import CodeSystemBase, ConceptBase, Concept
from .services import CodeSystemConceptsService
from core.util import get_rows_from_csv

router = APIRouter()

@router.get("/", response_model=CodeSystemBase)
async def root(concept_service: CodeSystemConceptsService = Depends()):
    response = CodeSystemBase(**CodeSystemBase.Config.schema_extra["example"])
    concepts = concept_service.get_concepts()
    concepts_base = [ConceptBase(**concept.dict()) for concept in concepts]
    response.concept = concepts_base
    return response

@router.get("/concepts", response_model=list[Concept])
async def concepts(concept_service: CodeSystemConceptsService = Depends()):
    concepts = concept_service.get_concepts()
    return concepts

@router.get("/$subsumes")
async def subsumes():
    return None

@router.get("/$validate-code")
def validate_code(url: str, codeSystem, code: str, version: str, display, coding: str, codeableConcept, date: str, abstract, displayLanguage: str):
    return { "Response" : "this is a validate code response"}

@router.get("/{id}/$validate-code")
async def validate_code(id):
    return { "Response" : "this is a validate code response for id %s" % id}

@router.get("/$lookup")
def look_up(code: str | None = None, system: str | None = None , version: str | None = None, coding: str | None = None, date: str  | None = None, displayLanguage: str | None = None, useSupplement: str | None = None, concept_service: CodeSystemConceptsService = Depends()):

    if (code is not None and system is None):
        return {
                    "resourceType": "OperationOutcome",
                    "id": "exception",
                    "text": {
                        "status": "additional",
                        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">The system parameter must be supplied if code is not empty.</div>"
                    },
                    "issue": [
                    {
                        "severity": "error",
                        "code": "not-found",
                        "details": {
                            "text": "The system parameter must be supplied if code is not empty."
                        }
                    }
                    ]
                }    
    
    code_system_concept = concept_service.get_concept_by_code(code)
    if (code_system_concept is not None):
        return {
            "resourceType" : "Parameters",
            "parameter": [
                {
                    "name" : "name",
                    "valueString": code_system_concept.concept_name
                },
                {
                    "name": "display",
                    "valueString": code_system_concept.concept_class_id
                },
                {
                    "name": "definition",
                    "valueString": code_system_concept.domain_id
                }
            ]
        }
    else:
        return {
            "resourceType": "OperationOutcome",
            "id": "exception",
            "text": {
                "status": "additional",
                "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Code %s not found</div>" % code
            },
            "issue": [
            {
                "severity": "error",
                "code": "not-found",
                "details": {
                    "text": "Code %s not found" % code
                }
            }
            ]
        }
    
@router.get("/{id}/$lookup")
def look_up(id, concept_service: CodeSystemConceptsService = Depends()):
    code_system_concept = concept_service.get_concept_by_id(id)    
    if (code_system_concept is not None):
        return {
            "resourceType" : "Parameters",
            "parameter": [
                {
                    "name" : "name",
                    "valueString": code_system_concept.concept_name
                },
                {
                    "name": "display",
                    "valueString": code_system_concept.concept_class_id
                },
                {
                    "name": "definition",
                    "valueString": code_system_concept.domain_id
                }
            ]
        }
    else:
        return {
            "resourceType": "OperationOutcome",
            "id": "exception",
            "text": {
                "status": "additional",
                "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Code %s not found</div>" % code
            },
            "issue": [
            {
                "severity": "error",
                "code": "not-found",
                "details": {
                    "text": "Code %s not found" % code
                }
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

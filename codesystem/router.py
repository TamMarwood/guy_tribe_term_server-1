from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

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
    # concepts = concept_service.get_concepts()
    # concepts = [CodeSystemConceptBase(**concept.dict()) for concept in concepts]
    # response.concept = concepts
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
async def subsumes():
    return 'this is subsumes response'

@router.get("/$validate-code")
async def validate_code():
    return { "Response" : "this is a validate code response"}

@router.get("/CodeSystem/$lookup")
def look_up():
    return {"Hello": "World"}

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

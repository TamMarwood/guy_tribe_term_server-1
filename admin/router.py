from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

from codesystem.schemas import CodeSystemBase, ConceptBase, Concept
from codesystem.services import CodeSystemConceptsService
from core.util import get_rows_from_csv

router = APIRouter()

@router.get("/concepts/recreate")
async def concepts_recreate(concept_service: CodeSystemConceptsService = Depends()):
    concept_rows = get_rows_from_csv('data/concepts.csv')
    # Drop table and recreate
    concept_service.recreate_concept_table()
    concepts: list[Concept] = []
    for row in concept_rows:
        concept_base = ConceptBase(**row)
        concepts.append(concept_base)
        concept_service.create_concept(concept_base)
    return concepts
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

from codesystem.schemas import CodeSystemBase, ConceptBase, Concept, ConceptRelationshipBase
from codesystem.services import CodeSystemConceptsService, CodeSystemConceptRelationshipService
from core.util import get_rows_from_csv

router = APIRouter()
# CONCEPTS
@router.get("/concepts/recreate")
async def concepts_recreate(service: CodeSystemConceptsService = Depends()):
    concept_rows = get_rows_from_csv('data/concepts.csv')
    # Drop table and recreate
    service.recreate_concept_table()
    concepts: list[Concept] = []
    for row in concept_rows:
        concept_base = ConceptBase(**row)
        concepts.append(concept_base)
        service.create_concept(concept_base)
    return concepts

# CONCEPT_RELATIONSHIPS
@router.get("/relationships/recreate")
async def concept_relationsips_recreate(service: CodeSystemConceptRelationshipService = Depends()):
    relationship_rows = get_rows_from_csv('data/relationships.csv')
    # Drop table and recreate
    service.recreate_table()
    concepts: list[Concept] = []
    for row in relationship_rows:
        relationship = ConceptRelationshipBase(**row)
        concepts.append(relationship)
        service.create_relationship(relationship)
    return concepts
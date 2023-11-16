from typing import List, Optional, Union
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import Table
from .schemas import Concept, ConceptBase, ConceptRelationship, ConceptRelationshipBase
from .models import Concept as ConceptDb, ConceptRelationship as ConceptRelationshipDb
from core.database import get_db, Base, engine

class CodeSystemConceptsService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    # Drop table and create again
    def recreate_concept_table(self):
        # Define the 'concept' table
        table = Table('concept', Base.metadata)
        table.drop(bind=engine, checkfirst=True)
        # Create the 'concept' table if it doesn't exist
        table.create(bind=engine, checkfirst=True)

    # def get_items(self) -> List[Item]:
    def get_concepts(self) -> List[Concept]:
        return self.db.query(ConceptDb).all()
    
    def get_concept_by_code(self, code) -> Concept:
        return self.db.query(ConceptDb).filter(ConceptDb.concept_code == code).first()

    def get_concept_by_id(self, id) -> Concept:
        return self.db.query(ConceptDb).filter(ConceptDb.concept_id == id).first()

    def create_concept(self, concept: ConceptBase) -> Union[Concept, None]:
        db_concept = self.db.query(ConceptDb).filter(ConceptDb.concept_code == concept.concept_code).first()
        if not db_concept:
            db_concept = ConceptDb(**concept.dict())
            self.db.add(db_concept)
            self.db.commit()
            self.db.refresh(db_concept)
            return db_concept

    # def get_item(self, item_id: int) -> Optional[Item]:
    #     return self.db.query(Item).filter(Item.id == item_id).first()

    # def update_item(self, item_id: int, item: ItemUpdate) -> Optional[Item]:
    #     db_item = self.db.query(Item).filter(Item.id == item_id).first()
    #     if db_item:
    #         for field, value in item.dict(exclude_unset=True).items():
    #             setattr(db_item, field, value)
    #         self.db.commit()
    #         self.db.refresh(db_item)
    #     return db_item

    # def delete_item(self, item_id: int) -> Optional[Item]:
    #     db_item = self.db.query(Item).filter(Item.id == item_id).first()
    #     if db_item:
    #         self.db.delete(db_item)
    #         self.db.commit()
    #     return db_item

class CodeSystemConceptRelationshipService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    
    # Drop table and create again
    def recreate_table(self):
        # Define the 'concept' table
        table = Table('concept_relationship', Base.metadata)
        table.drop(bind=engine, checkfirst=True)
        # Create the 'concept' table if it doesn't exist
        table.create(bind=engine, checkfirst=True)

    def create_relationship(self, relationship: ConceptRelationshipBase):
        db_concept_relationship = ConceptRelationshipDb(**relationship.dict())
        self.db.add(db_concept_relationship)
        self.db.commit()
        self.db.refresh(db_concept_relationship)
        return db_concept_relationship
    
    def get_relationship_by_code(self, code, a_or_b: str):
        if a_or_b == 'a':
            return self.db.query(ConceptRelationshipDb).filter(ConceptRelationshipDb.concept_id_1 == code).first()
        else:
            return self.db.query(ConceptRelationshipDb).filter(ConceptRelationshipDb.concept_id_2 == code).first()
    
    def get_relationship_by_codeA_codeB(self, codeA, codeB):
        return self.db.query(ConceptRelationshipDb).filter(ConceptRelationshipDb.concept_id_1 == codeA, ConceptRelationshipDb.concept_id_2 == codeB).first()
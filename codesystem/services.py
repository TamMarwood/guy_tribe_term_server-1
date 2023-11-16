from typing import List, Optional, Union
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import Table
from .schemas import Concept, ConceptBase
from .models import Concept as CodeSystemConceptDb
from core.database import get_db, Base, engine

class CodeSystemConceptsService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    # Drop table and create again
    def recreate_concept_table(self):
        # Define the 'items' table
        ConceptTable = Table('concept', Base.metadata)
        ConceptTable.drop(bind=engine, checkfirst=True)
        # Create the 'items' table if it doesn't exist
        ConceptTable.create(bind=engine, checkfirst=True)
        # self.db.commit()

    # def get_items(self) -> List[Item]:
    def get_concepts(self) -> List[Concept]:
        return self.db.query(CodeSystemConceptDb).all()
    
    def get_concept_by_code(self, code) -> Concept:
        return self.db.query(CodeSystemConceptDb).filter(CodeSystemConceptDb.concept_code == code).first()

    def get_concept_by_id(self, id) -> Concept:
        return self.db.query(CodeSystemConceptDb).filter(CodeSystemConceptDb.concept_id == id).first()

    def create_concept(self, concept: ConceptBase) -> Union[Concept, None]:
        db_concept = self.db.query(CodeSystemConceptDb).filter(CodeSystemConceptDb.concept_code == concept.concept_code).first()
        if not db_concept:
            db_concept = CodeSystemConceptDb(**concept.dict())
            self.db.add(db_concept)
            self.db.commit()
            self.db.refresh(db_concept)
            return db_concept

    # def create_item(self, item: ItemCreate) -> Item:
    #     db_item = Item(**item.dict())
    #     self.db.add(db_item)
    #     self.db.commit()
    #     self.db.refresh(db_item)
    #     return db_item

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

from typing import List, Optional, Union
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from .schemas import CodeSystemConcept, CodeSystemConceptBase
from .models import CodeSystemConcept as CodeSystemConceptDb
from core.database import get_db

class CodeSystemService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    # def get_items(self) -> List[Item]:
    def get_items(self):
        return {'aaa':'sss'}
        # return self.db.query(Item).all()

class CodeSystemConceptsService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    # def get_items(self) -> List[Item]:
    def get_concepts(self) -> List[CodeSystemConcept]:
        return self.db.query(CodeSystemConceptDb).all()
    
    def create_concept(self, concept: CodeSystemConceptBase) -> Union[CodeSystemConcept, None]:
        db_concept = self.db.query(CodeSystemConceptDb).filter(CodeSystemConceptDb.code == concept.code).first()
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

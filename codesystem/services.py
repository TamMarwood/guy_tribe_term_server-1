from typing import List, Optional
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from .models import CodeSystemConcept, CodeSystem
from core.database import get_db

class CodeSystemService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    # def get_items(self) -> List[Item]:
    def get_items(self):
        return {'aaa':'sss'}
        # return self.db.query(Item).all()

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

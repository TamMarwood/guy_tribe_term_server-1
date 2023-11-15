from fastapi import APIRouter, HTTPException, Depends
from typing import List

from .models import CodeSystem
from .services import CodeSystemService

router = APIRouter()

# @router.post("/", response_model=Item)
# async def create_item(item: ItemCreate, code_system_service: CodeSystemService = Depends()):
#     return code_system_service.create_item(item)

# @router.get("/", response_model=List[Item])
# @router.get("/")
# async def read_items(code_system_service: CodeSystemService = Depends()):
#     return code_system_service.get_items()

@router.get("/")
async def read_items():
    return 'aaaa'

@router.get("/$subsumes")
async def subsumes():
    return 'this is subsumes response'

@router.get("/<id>/$subsumes")
async def subsumes_by_id(id ):
    return { "Response" : "this is a subsumes id response with id value %s" % id}

@router.get("/$validate-code")
async def validate_code():
    return { "Response" : "this is a validate code response"}

@router.get("/<id>/$validate-code")
async def validate_code_by_id(id):
    return { "Response" : "this is a validate code by id response with id value %s" % id}

@router.get("/CodeSystem/$lookup")  
def look_up():
    return {"Hello": "World"}    

# @router.get("/{item_id}", response_model=Item)
# async def read_item(item_id: int, item_service: ItemService = Depends()):
#     return item_service.get_item(item_id)

# @router.put("/{item_id}", response_model=Item)
# async def update_item(item_id: int, item: ItemUpdate, item_service: ItemService = Depends()):
#     return item_service.update_item(item_id, item)

# @router.delete("/{item_id}", response_model=Item)
# async def delete_item(item_id: int, item_service: ItemService = Depends()):
#     return item_service.delete_item(item_id)

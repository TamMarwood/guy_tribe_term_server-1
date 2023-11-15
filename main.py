from fastapi import FastAPI
from codesystem.router import router as codesystem_router#, user_router
# from valueset.router import router as valueset_router#, user_router
from core.config import settings

app = FastAPI()

# Include routers
app.include_router(codesystem_router, prefix="/CodeSystem", tags=["CodeSystem"])
# app.include_router(valueset_router, prefix="/ValueSet", tags=["ValueSet"])
# app.include_router(item_router, prefix="/items", tags=["items"])

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", reload=True, port=settings.app_port)

# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/CodeSystem")
# def read_root():
#     return {"Hello": "World"}
# @app.get("/CodeSystem/$lookup")
# def read_root():
#     return {"Hello": "World"}
# @app.get("/CodeSystem/$validate-code")
# def read_root():
#     return {"Hello": "World"}
# @app.get("/CodeSystem/$subsumes")
# def read_root():
#     return {"Hello": "World"}
# @app.get("/CodeSystem/$validate")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/ValueSet/$expand")
# def read_root():
#     return {"Hello": "World"}
# @app.get("/ValueSet/$validate-code")
# def read_root():
#     return {"Hello": "World"}
# @app.get("/ValueSet/$validate")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
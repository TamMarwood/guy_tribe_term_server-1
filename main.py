from fastapi import FastAPI
from codesystem.router import router as codesystem_router#, user_router
# from valueset.router import router as valueset_router#, user_router
from core.config import settings
from core.database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(codesystem_router, prefix="/CodeSystem", tags=["CodeSystem"])
# app.include_router(valueset_router, prefix="/ValueSet", tags=["ValueSet"])

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", reload=True, port=settings.app_port)
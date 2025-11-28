from fastapi import FastAPI
from app.database import Base, engine
from app.routes.user_route import router as user_router

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "FastAPI with PostgreSQL is running!"}

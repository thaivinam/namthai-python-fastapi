from fastapi import FastAPI

from app.routers.vote import votes
from . import models
from .database import engine
from .routers import user, post, auth, vote

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}
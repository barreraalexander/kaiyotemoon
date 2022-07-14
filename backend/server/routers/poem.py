from fastapi import status, HTTPException, Response, Depends, APIRouter

from server import models, schemas
from server.database import get_db
from server.utils.get_poems import run as run_get_poems
from sqlalchemy.orm import Session

from typing import List


router = APIRouter(
    prefix="/poems",
    tags = ['Poems']
)

@router.get("/", response_model=List[schemas.Poem])
def get_poems():
    poems = run_get_poems()

    if not poems:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item was not found.")

    return poems


@router.get("/{id}", response_model=schemas.Poem)
def get_poem(id: int):
    try:
        poem = run_get_poems()[id]
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item was not found.")

    return poem

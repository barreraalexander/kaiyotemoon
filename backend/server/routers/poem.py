from fastapi import status, HTTPException, Response, Depends, APIRouter

from server import models, schemas
from server.database import get_db
from sqlalchemy.orm import Session

from typing import List

router = APIRouter(
    pref="/poems",
    tags = ['Poems']
)

@router.get("/", response_model=List[schemas.Poem])
def get_poems(db: Session = Depends(get_db)):
    poems = db.query(models.Poem).all()
    return poems

@router.get("/{id}", response_model=schemas.Poem)
def get_poem(id: int, db: Session=Depends(get_db)):
    poem = db.query(models.Poem).filter(models.Poem.id==id).first()

    if not poem:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item was not found")

    return poem


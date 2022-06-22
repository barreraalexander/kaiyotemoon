from fastapi import status, HTTPException, Response, Depends, APIRouter

from server import models, schemas
from server.database import get_db
from sqlalchemy.orm import Session

from typing import List

from server.utils.fill_database import run as run_fill_db

router = APIRouter(
    prefix="/poems",
    tags = ['Poems']
)

@router.get("/filldb", status_code=status.HTTP_201_CREATED)
def fill_db(db: Session = Depends(get_db)):
    poem_dicts = run_fill_db()
    for poem_dict in poem_dicts:
        poem = models.Poem(**poem_dict)
        db.add(poem)
        db.commit()
        # print (poem_dict, "\n\n")
        # print (poem.content, "\n\n")
    # print (poem_dicts)

    # print ('here')


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

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Poem)
def create_poem(poem: schemas.PoemCreate, db: Session = Depends(get_db)):
    new_poem = models.Poem(**poem.dict())

    db.add(new_poem)
    db.commit()
    db.refresh(new_poem)

    return new_poem


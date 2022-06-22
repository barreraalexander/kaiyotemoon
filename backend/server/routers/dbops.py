from fastapi import status, Depends, APIRouter

from server import models
from server.database import get_db
from sqlalchemy.orm import Session

from server.utils.fill_database import run as run_fill_db

router = APIRouter(
    prefix="/dbops",
    tags = ['Database Operations']
)

@router.get("/filldb", status_code=status.HTTP_201_CREATED)
def fill_db(db: Session = Depends(get_db)):
    poem_dicts = run_fill_db()
    for poem_dict in poem_dicts:
        poem = models.Poem(**poem_dict)
        db.add(poem)
        db.commit()


from typing import List
from fastapi import FastAPI, Depends, HTTPException
from db import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models 
import schemas

Base.metadata.create_all(engine)

app = FastAPI()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/Mybook{id}", response_model=schemas.Mybook)
def root_book(id: int, session: Session = Depends(get_session)):
    mybook = session.query(models.Mybook).get(id)

    return mybook

@app.post("/Mybook", response_model=schemas.Mybook)
def create_book(mybook: schemas.MybookCreate, session: Session = Depends(get_session)):
    mybookdb = models.Mybook(
        title = mybook.title,
        author = mybook.author,
        description = mybook.description
    )
    session.add(mybookdb)
    session.commit()

    return mybookdb

@app.patch("/Mybook")
def update_book():
    return "update book item"

@app.delete("/Mybook/{id}", response_model=schemas.Deletebook)
def delete_book(id: int, session: Session = Depends(get_session)):
    mybook = session.query(models.Mybook).get(id)

    if not mybook:
        raise HTTPException(status_code=404, detail="mybook not found")
    
    session.delete(mybook)
    session.commit()

    return {"ok": True}



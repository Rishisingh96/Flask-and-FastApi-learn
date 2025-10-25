from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from models import ToDo
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()


class ToDoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False


class ToDoResponse(ToDoCreate):
    id: int

    class Config:
        orm_mode = True


@router.get('/', response_model=List[ToDoResponse])
def show_todos(db: Session = Depends(get_db)):
    return db.query(ToDo).all()


@router.post('/', response_model=ToDoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: ToDoCreate, db: Session = Depends(get_db)):
    new_todo = ToDo(title=todo.title, description=todo.description, done=todo.done)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@router.put('/{todo_id}', response_model=ToDoResponse)
def update_todo(todo_id: int, updated: ToDoCreate, db: Session = Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    todo.title = updated.title
    todo.description = updated.description
    todo.done = updated.done
    db.commit()
    db.refresh(todo)
    return todo


@router.delete('/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    db.delete(todo)
    db.commit()
    return {"message":"Delete successfully...."}

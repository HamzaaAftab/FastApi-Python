from fastapi import APIRouter, Depends
from database import get_database
from models import Todo
from bson import ObjectId

router = APIRouter()

@router.post("/add/")
async def add_todo(todo: Todo, db=Depends(get_database)):
    new_todo = await db.todos.insert_one(todo.dict())
    return {"id": str(new_todo.inserted_id)}

@router.get("/todos/")
async def get_todos(db=Depends(get_database)):
    todos = await db.todos.find().to_list(None)
    return [{"id": str(todo["_id"]), "title": todo["title"], "description": todo["description"], "completed": todo["completed"]} for todo in todos]

@router.put("/update/{todo_id}")
async def update_todo(todo_id: str, todo: Todo, db=Depends(get_database)):
    await db.todos.update_one({"_id": ObjectId(todo_id)}, {"$set": todo.dict()})
    return {"message": "Todo updated"}

@router.delete("/delete/{todo_id}")
async def delete_todo(todo_id: str, db=Depends(get_database)):
    await db.todos.delete_one({"_id": ObjectId(todo_id)})
    return {"message": "Todo deleted"}

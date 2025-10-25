# # ===========================================
# # 📘 To-Do List API using FastAPI
# # Author: Rishi Singh
# # Description: Simple CRUD API to manage a To-Do list
# # ===========================================

# # --- Import Required Libraries ---
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List, Optional

# # --- Create FastAPI App Instance ---
# app = FastAPI(
#     title="To-Do List API",
#     description="A simple REST API for managing To-Do tasks using FastAPI",
#     version="1.0.0"
# )

# # --- Pydantic Model for To-Do Item ---
# class ToDo(BaseModel):
#     id: int                    # Unique ID for each To-Do
#     name: str                  # Title or short name of the task
#     description: Optional[str] = None   # Task details (optional)


# # --- In-Memory Database (Temporary) ---
# # In real applications, you’ll use a database like MySQL, PostgreSQL, or MongoDB
# todos: List[ToDo] = []


# # ===========================================
# # 🟩 READ OPERATION – Get all To-Dos
# # ===========================================
# @app.get("/", response_model=List[ToDo])
# def get_all_todos():
#     """
#     Fetch all existing To-Dos.
#     Returns a list of all tasks stored in memory.
#     """
#     return todos


# # ===========================================
# # 🟦 CREATE OPERATION – Add a new To-Do
# # ===========================================
# @app.post("/", status_code=201)
# def create_todo(todo: ToDo):
#     """
#     Create a new To-Do and add it to the list.
#     """
#     # Check if the ID already exists
#     for existing in todos:
#         if existing.id == todo.id:
#             raise HTTPException(status_code=400, detail="To-Do with this ID already exists.")

#     todos.append(todo)
#     return {"message": "✅ To-Do created successfully!", "data": todo}


# # ===========================================
# # 🟨 UPDATE OPERATION – Modify existing To-Do
# # ===========================================
# @app.put("/{todo_id}")
# def update_todo(todo_id: int, updated_todo: ToDo):
#     """
#     Update an existing To-Do by its ID.
#     """
#     for index, todo in enumerate(todos):
#         if todo.id == todo_id:
#             todos[index] = updated_todo
#             return {"message": "✏️ To-Do updated successfully!", "data": updated_todo}

#     # If not found
#     raise HTTPException(status_code=404, detail="To-Do not found.")


# # ===========================================
# # 🟥 DELETE OPERATION – Remove a To-Do
# # ===========================================
# @app.delete("/{todo_id}")
# def delete_todo(todo_id: int):
#     """
#     Delete a To-Do by its ID.
#     """
#     global todos
#     new_todos = [todo for todo in todos if todo.id != todo_id]

#     if len(new_todos) == len(todos):
#         raise HTTPException(status_code=404, detail="To-Do not found.")

#     todos = new_todos
#     return {"message": "🗑️ To-Do deleted successfully!"}


# # ===========================================
# # 🟧 (Optional) GET SINGLE TODO by ID
# # ===========================================
# @app.get("/{todo_id}", response_model=ToDo)
# def get_single_todo(todo_id: int):
#     """
#     Fetch a single To-Do by its ID.
#     """
#     for todo in todos:
#         if todo.id == todo_id:
#             return todo
#     raise HTTPException(status_code=404, detail="To-Do not found.")

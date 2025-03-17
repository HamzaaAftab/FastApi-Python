from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from database import get_database
from routes.todo_routes import router as todo_router
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static files (CSS & JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load templates
templates = Jinja2Templates(directory="templates")

# Include API routes for CRUD operations
app.include_router(todo_router)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db=Depends(get_database)):
    todos = await db.todos.find().to_list(None)
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

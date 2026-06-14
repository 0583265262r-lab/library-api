from fastapi import APIRouter,FastAPI
from routes import book_routes
import uvicorn

app = FastAPI()
router = APIRouter()

app.include_router(book_routes.router)
if __name__ == "__main__":
    uvicorn.run(app="main:app",reload=True)
 
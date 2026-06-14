from fastapi import HTTPException,APIRouter
from databases import book_db
from pydantic import BaseModel
import uvicorn
bookdb = book_db.BookDB()
router = APIRouter()
class CreateBook(BaseModel):
    title: str 
    author: str 
    genre: str

@router.post("/books")
def create_book(data : CreateBook):
    try:
        add_book = bookdb.create_book({"title":data.title,"author":data.author,"genre":data.genre})
        return f"add book {add_book} was success "
    except: 
        raise HTTPException(status_code=404)



@router.get("/books")
def get_all_books():
    all_books = bookdb.get_all_books()
    return all_books
    
@router.get("/books/{id}")
def get_book_by_id(id:int):
    try:
        return bookdb.get_book_by_id(id)
    except:
        raise HTTPException(status_code=404,detail="id not found")
class UpdateBook(BaseModel):
        title: str |None = None
        author: str |None = None
        genre: str |None = None
        available_is: bool |None = None
        borrowed_by_member_id: int |None = None

@router.put("/books/{id}")
def update_book_by_id(id:int,data:UpdateBook):
    try:
        update = bookdb.update_book(id,data)
        return update
    except:
        raise HTTPException(status_code=404)


if __name__ == "__main__":
    uvicorn.run(router="book_routes:router",reload=True)
    


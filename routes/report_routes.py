from fastapi import HTTPException,APIRouter
from databases import member_db,book_db
from pydantic import BaseModel
import uvicorn
bookdb = book_db.BookDB()
memberdb = member_db.MemberDB()
router = APIRouter()

@router.get("/reports/summary")
def general_reports():
    
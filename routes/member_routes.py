from fastapi import HTTPException,APIRouter
from databases import member_db
from pydantic import BaseModel
import uvicorn

memberdb = member_db.MemberDB()
router = APIRouter()

class MemberIn(BaseModel):
    name:str
    email: str

@router.post("/members")
def create_member(data:MemberIn):
    try:
        add_member = memberdb.create_member(data.model_dump())
        return f"add member {add_member} was success "
    except: 
        raise HTTPException(status_code=404)
    
@router.get("/members")
def get_all_members():
    all_members = memberdb.get_all_members()
    return all_members

@router.get("/members/{id}")
def get_member_by_id(id):
    try:
        get_member = memberdb.get_member_by_id(id)
        return get_member
    except:
        raise HTTPException(status_code=404,detail="member not found")

class MemberUpdating(BaseModel):
    name:str |None = None
    email: str |None = None
    is_active :bool |None = None
    total_borrows : int |None = None

@router.put("/members/{id}")
def update_member_by_id(id:int,body:MemberUpdating):
    try:
        data = body.model_dump(exclude_unset=True)
        update = memberdb.update_member(id,data)
        return update
    except :
        raise HTTPException(status_code=404)

@router.put("/members/{id}/deactivate")
def deactivate_member(id:int):
    try:
        update = memberdb.deactivate_member(id)
        return update
    except :
        raise HTTPException(status_code=404)
    
@router.put("/members/{id}/activate")
def activate_member(id:int):
    try:
        update = memberdb.activate_member(id)
        return update
    except :
        raise HTTPException(status_code=404)
    
from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Annotated

router = APIRouter()

@router.get("/all_users", tags=["users"])
async def get_all_user(): #READ
    pass

@router.get("/user", tags=["users"])
async def get_user(): #READ
    pass

@router.post("/user", tags=["users"])
async def add_user(): #CREATE
    pass
@router.put("/user", tags=["users"])
async def update_user(): #UPDATE
    pass

@router.delete("/user", tags=["users"])
async def remove_user(user_id:str): #DELETE
    pass
from Auth.AuthHandler import Authentication_Authorization
from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Annotated

router = APIRouter()
auth_worker = Authentication_Authorization()

@router.get("/all_users", tags=["users"])
async def get_all_user(): #READ
    return {"results":[]}

@router.get("/user", tags=["users"])
async def get_user(): #READ
    return {"results":[]}

@router.post("/user", tags=["users"])
async def add_user(): #CREATE
    return {"results":[]}


@router.put("/user", tags=["users"])
async def update_user(): #UPDATE
    return {"results":[]}

@router.delete("/user", tags=["users"])
async def remove_user(user_id:str): #DELETE
    return {"results":[]}


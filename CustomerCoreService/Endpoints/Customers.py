from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Annotated


router = APIRouter()

@router.get("/all_customers")
async def get_all_customers(): #READ
    
    return {"results":[]}

@router.get("/customer")
async def get_customer(): #READ
    return {"results":[]}

@router.post("/customer")
async def add_customer(): #CREATE
    
    return {"results":[]}

@router.put("/customer")
async def update_customer(): #UPDATE

    return {"results":[]}

@router.delete("/customer")
async def remove_customer(user_id:str): #DELETE
    
    return {"results":[]}
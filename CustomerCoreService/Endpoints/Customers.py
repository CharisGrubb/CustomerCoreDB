from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Annotated


router = APIRouter()

@router.get("/all_customers")
async def get_all_customers(): #READ
    pass

@router.get("/customer")
async def get_customer(): #READ
    pass

@router.post("/customer")
async def add_customer(): #CREATE
    pass
@router.put("/customer")
async def update_customer(): #UPDATE
    pass

@router.delete("/customer")
async def remove_customer(user_id:str): #DELETE
    pass
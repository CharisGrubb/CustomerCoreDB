from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Annotated


router = APIRouter()

@router.get("/all_customers")
async def get_all_customers(): #READ
    
    return {"results":[]}

@router.get("/customer")
async def get_customer(customer_id:str): #READ
    return {"results":[]}

@router.post("/customer")
async def add_customer( email_address:str, phone_number:str, first_name:str, last_name:str, middle_name:str=None): #CREATE
    
    return {"results":[]}

@router.put("/customer")
async def update_customer(customer_id:str, update_fields:dict): #UPDATE

    return {"results":[]}

@router.delete("/customer")
async def remove_customer(customer_id:str): #DELETE

    return {"results":[]}
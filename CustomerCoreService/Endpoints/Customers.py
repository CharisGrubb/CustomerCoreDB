from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Annotated
from Auth.AuthHandler import Authentication_Authorization


router = APIRouter()
auth = Authentication_Authorization()

@router.get("/all_customers")
async def get_all_customers(): #READ

    #Authenticate user

    #pull data

    #Return results
    return {"results":[], "total":0}

@router.get("/customer")
async def get_customer(customer_id:str): #READ
    #Authenticate User

    #Validate Input

    #Pull data

    #Return to user
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
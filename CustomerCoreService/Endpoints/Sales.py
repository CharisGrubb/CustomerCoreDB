from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Annotated

router = APIRouter()



@router.get("/sales_by_user")
async def get_sales_by_user(include_projection = False): #READ
    return {"results":[]}
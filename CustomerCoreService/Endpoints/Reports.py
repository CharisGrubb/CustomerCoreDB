from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Annotated

router = APIRouter()



@router.get("/added_user_trend")
async def get_added_users(include_projection = False): #READ
    return {"results":[]}
from fastapi import APIRouter

router = APIRouter()


@router.get("/user")
async def get_user(): #READ
    pass

@router.post("/user")
async def add_user(): #CREATE
    pass
@router.put("/user")
async def update_user(): #UPDATE
    pass

@router.delete("/user")
async def remove_user(user_id:str): #DELETE
    pass
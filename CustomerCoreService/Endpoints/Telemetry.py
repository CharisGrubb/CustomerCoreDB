
from fastapi import APIRouter


router = APIRouter()


@router.get("/logs")
async def get_logs(log_type:str): #READ
    if log_type not in ['INFO','WARN','ALERT','ERROR']:
        print("BAD LOG TYPE")


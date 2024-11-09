from fastapi import FastAPI 

from .Endpoints import Customers, Telemetry, Users


app = FastAPI() 

app.include_router(Customers.router)
app.include_router(Telemetry.router)
app.include_router(Users.router)
from Endpoints import Customers, Users, Sales
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from opentelemetry import sdk, trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor




trace.set_tracer_provider(TracerProvider(resource = sdk.resources.Resource.create({sdk.resources.SERVICE_NAME:"CustomerCore"})))
trace_provider = trace.get_tracer_provider()


app = FastAPI() 
FastAPIInstrumentor.instrument_app(app)

origins = ["http://localhost"
           , "http://localhost:8000"
           ,"https://cdn-script.com/ajax/libs/jquery/3.7.1/jquery.js"]

app.add_middleware(CORSMiddleware
                   , allow_origins = origins
                   , allow_credentials=True
                   ,allow_methods=["*"] #allow GET, POST, PUT, etc
                   ,allow_headers=["*"]) #FILTER METHODS AND HEADERS LATER AFTER FULLY FUNCTIONAL

app.include_router(Customers.router)
app.include_router(Users.router)
app.include_router(Sales.router)


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    print('Inside html call')
    id = 9999
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id}
    )

@app.get("/login", response_class=HTMLResponse)
async def log_in(request: Request):
    print('Inside html call')
    return templates.TemplateResponse(
        request=request, name="login.html")

@app.get("/menu", response_class=HTMLResponse)
async def load_menu(request: Request):
    print('Inside menu call')
    return templates.TemplateResponse(
        request=request, name="menu.html")
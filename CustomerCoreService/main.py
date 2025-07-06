from Endpoints import Customers, Users, Sales
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from Logging.Logger import Logger
from opentelemetry import sdk, trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor




trace.set_tracer_provider(TracerProvider(resource = sdk.resources.Resource.create({sdk.resources.SERVICE_NAME:"CustomerCore"})))
trace_provider = trace.get_tracer_provider()


app = FastAPI() 
FastAPIInstrumentor.instrument_app(app)
log = Logger("Main","Fast API Manager")

origins = ["http://localhost" 
           , "http://localhost:8000"
           ,"https://cdn-script.com/ajax/libs/jquery/3.7.1/jquery.js"]

app.add_middleware(CORSMiddleware
                   , allow_origins = origins
                   , allow_credentials=True
                   ,allow_methods=["*"] #allow GET, POST, PUT, etc
                   ,allow_headers=["*"]) #FILTER METHODS AND HEADERS LATER AFTER FULLY FUNCTIONAL


#API Endpoints
app.include_router(Customers.router)
app.include_router(Users.router)
app.include_router(Sales.router)


app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/templates/images", StaticFiles(directory="templates"), name="images")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    log.log_to_database("home","INFO","inside home page",None)
    total_cust = 101
    return templates.TemplateResponse(
        request=request, name="index.html", context={"total_cust_num": total_cust
                                                    ,"total_cust_trend":"LOADING..."}
    )

@app.get("/login", response_class=HTMLResponse)
async def log_in(request: Request):
    return templates.TemplateResponse(
        request=request, name="login.html")

@app.get("/logout", response_class=HTMLResponse)
async def log_out(request: Request):

    #remove cookie session

    #send back to log in page
    return templates.TemplateResponse(
        request=request, name="login.html")

@app.get("/reports", response_class=HTMLResponse)
async def log_in(request: Request):
    return templates.TemplateResponse(
        request=request, name="reports.html")



#Inner calls for sub pieces
@app.get("/menu", response_class=HTMLResponse, include_in_schema=False)
async def load_menu(request: Request):
    return templates.TemplateResponse(
        request=request, name="menu.html")


@app.get("/header", response_class=HTMLResponse, include_in_schema=False)
async def load_menu(request: Request):
    return templates.TemplateResponse(request=request, name="header.html", context={"user_name":"test username"})

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('templates/images/favicon.ico')
from Endpoints import Customers, Users, Sales
from fastapi import FastAPI, Request
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
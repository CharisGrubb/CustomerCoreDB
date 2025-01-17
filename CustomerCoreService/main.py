from .Endpoints import Customers, Users
from fastapi import FastAPI 
from opentelemetry import sdk, trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor




trace.set_tracer_provider(TracerProvider(resource = sdk.resources.Resource.create({sdk.resources.SERVICE_NAME:"CustomerCore"})))
trace_provider = trace.get_tracer_provider()


app = FastAPI() 
FastAPIInstrumentor.instrument_app(app)

app.include_router(Customers.router)
app.include_router(Users.router)
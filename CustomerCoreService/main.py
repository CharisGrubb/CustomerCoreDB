from Endpoints import Customers, Telemetry, Users
from fastapi import FastAPI 
from opentelemetry import sdk 
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor




sdk.trace.set_trace_profider(sdk.trace.TraceProvider(resource = sdk.resources.Resource.create({sdk.resources.SERVICE_NAME:"CustomerCore"})))
trace_provider = sdk.trace.get_tracer_provider()


app = FastAPI() 
FastAPIInstrumentor.instrument_app(app)

app.include_router(Customers.router)
app.include_router(Telemetry.router)
app.include_router(Users.router)
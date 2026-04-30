from fastapi import FastAPI, HTTPException
from .core.schemas import QueryRequest, QueryResponse
from .agent.orchestrator import AgentOrchestrator
from .core.settings import settings

app = FastAPI(title=settings.APP_NAME)
orchestrator = AgentOrchestrator()

@app.get("/")
def read_root():
    return {"message": f"Welcome to the {settings.APP_NAME} API"}

@app.post("/process", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    try:
        response = orchestrator.run(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

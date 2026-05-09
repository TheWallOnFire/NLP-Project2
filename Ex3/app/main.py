from fastapi import FastAPI, HTTPException
from .core.schemas import QueryRequest, QueryResponse
from .agent.orchestrator import AgentOrchestrator
from .core.settings import settings

import logging
import os

# Configure logging based on DEBUG env var
debug_mode = os.getenv("DEBUG", "false").lower() == "true"
logging.basicConfig(
    level=logging.DEBUG if debug_mode else logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("banking-api")

app = FastAPI(title=settings.APP_NAME)
orchestrator = AgentOrchestrator()

@app.get("/")
def read_root():
    return {"message": f"Welcome to the {settings.APP_NAME} API"}

@app.post("/process", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    logger.info(f"Received request: {request.query}")
    try:
        response = orchestrator.run(request)
        logger.info(f"Successfully processed request. Decision: {response.trace.router.decision}")
        return response
    except Exception as e:
        logger.error(f"Error processing request: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

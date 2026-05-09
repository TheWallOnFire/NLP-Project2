import uvicorn
import os
from pathlib import Path

def main():
    """Run the Banking AI-Agent server."""
    # Get project root
    project_root = Path(__file__).parent
    
    # Configuration
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    debug_mode = os.getenv("DEBUG", "false").lower() == "true"
    log_level = "debug" if debug_mode else "info"
    
    # Run server
    uvicorn.run( 
        "app.main:app",
        host=host,
        port=port,
        reload=debug_mode,
        log_level=log_level
    )

if __name__ == "__main__":
    main()

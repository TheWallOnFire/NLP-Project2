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
    debug_mode = os.getenv("DEBUG", "true").lower() == "true"
    log_level = "debug" if debug_mode else "info"
    
    # Run server
    uvicorn.run( 
        "app.main:app",
        host=host,
        port=port,
        reload=debug_mode,
        reload_dirs=["app"],  # Only watch the 'app' directory for changes
        reload_excludes=["unsloth_compiled_cache/*", "venv/*", "*.pyc"],
        log_level=log_level
    )

if __name__ == "__main__":
    main()

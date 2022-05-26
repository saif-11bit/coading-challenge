import uvicorn
import os
from application import app
from api.api_router import api_router
from utils.app_event_funcs import shutdown, startup

app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)

app.include_router(api_router)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        "application:app",
        host="0.0.0.0",
        port=port,
        log_level="info",
        loop="asyncio",
        reload=True,
        lifespan="on"
    )

import uvicorn
from config import PORT, BIND, WORKERS, RELOAD
import uvicorn

from config import PORT, BIND, WORKERS, RELOAD

if __name__ == "__main__":
    uvicorn.run(
        "api:app",
        host=BIND,
        port=int(PORT),
        workers=int(WORKERS),
        reload = RELOAD,
        debug=RELOAD

    )
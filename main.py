import uvicorn
from api.router.api import router
from fastapi import FastAPI


app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, port=8001)

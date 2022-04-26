import uvicorn
from api.router.api import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)


@app.get("/")
async def root():
    return {"message" : "welcome to your blog! "}


if __name__ == "__main__":
    uvicorn.run(app, port=8001)

from fastapi import FastAPI
import uvicorn
from routers import articles


app = FastAPI()
app.include_router(articles.router)

if __name__ == '__main__':
    # reload
    uvicorn.run("main:app", reload=True)

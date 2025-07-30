from fastapi import FastAPI
from routes import blog_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Blog API"}

app.include_router(blog_router)

from fastapi import APIRouter

blog_router = APIRouter()

@blog_router.get("/posts")
def get_posts():
    return [{"id": 1, "title": "First Post"}]

@blog_router.post("/posts")
def create_post():
    return {"message": "New post created"}

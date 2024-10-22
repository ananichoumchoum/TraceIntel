from fastapi import APIRouter
from app.services.twitter_service import search_twitter

router = APIRouter()

@router.get("/scan")
def scan_social_media(keyword: str):
    result = search_twitter(keyword)
    return {"result": result}
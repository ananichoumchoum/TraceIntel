from fastapi import FastAPI
from app.api import social_media, image_analysis

# Initialize the FastAPI app
app = FastAPI()

# Include the routers from the 'api' folder
app.include_router(social_media.router, prefix="/social-media", tags=["Social Media"])
app.include_router(image_analysis.router, prefix="/image", tags=["Image Analysis"])

@app.get("/")
def read_root():
    return {"message": "Welcome to TraceIntel!"}

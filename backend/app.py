from fastapi import FastAPI
from api.urlShortner_api import url_shorten_router
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost",
    "http://localhost:8000",
]



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(url_shorten_router)

@app.get("/")
def home():
    return {"message":"URL Shortening service welcomes you...."}




from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.series import router
from starlette.middleware.sessions import SessionMiddleware
import os

app = FastAPI(title="YeriScan")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#none and false
app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY"),
    same_site = "lax",
    https_only=False
)


app.include_router(router, prefix="/series") 



@app.get("/")
def read_root():
    return {"message": "YeriScans"}
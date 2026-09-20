from fastapi import FastAPI
from Routes.studentroutes import router
from fastapi.middleware.cors import CORSMiddleware

app  = FastAPI()

# origin  = ["http://localhost:5173",
#         "http://127.0.0.1:5173",
#         "https://rainbow-beignet-124f09.netlify.app",
#         ]

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"] ,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def greet():
    return {"message":"hello"}
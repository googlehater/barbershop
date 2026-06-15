from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth_router, appointments_router, admin_router
from app.api import services_router

app = FastAPI(title="Barbershop API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router, prefix="/api")
app.include_router(appointments_router.router, prefix="/api")
app.include_router(admin_router.router, prefix="/api")
app.include_router(services_router.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Barbershop API is running"}

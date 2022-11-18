from fastapi import APIRouter
from apis.version1 import route_comm

api_router = APIRouter()
api_router.include_router(route_comm.router, prefix="/comm", tags=["comm"])

# If more APIs are added, we can add more routers here.

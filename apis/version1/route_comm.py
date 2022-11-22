from fastapi import APIRouter
from schemas.sch_comm import RequestEmailSch
from apis.utils.utils import send_email

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello Mailing Mircoservice"}


@router.post("/send_email")
async def send_email_router(info: RequestEmailSch):
    print(RequestEmailSch)
    send_email(info.user_email, info.title, info.content)
    return True


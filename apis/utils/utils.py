from optparse import Option
from pydantic import EmailStr
from config.config import settings
from typing import Optional

import requests


def send_email(mail_address: EmailStr, title: str, content: Optional[str]):

    res = requests.post("")

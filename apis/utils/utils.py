from optparse import Option
from pydantic import EmailStr
from config.config import settings
from typing import Optional

import requests


def send_email(mail_address: EmailStr, title: str, content: Optional[str]):

    res = requests.post(
        "https://api.mailgun.net/v3/project4.org/messages",
        auth=("api", settings.EMAIL_API_KEY),
        data={
            "from": "Happy User <mailgun@project4.org>",
            "to": [mail_address],
            "subject": title,
            "text": content,
        },
    )

    print(res.status_code)

    if res.status_code == 200:
        print("Email sent successfully")
        return True

    return False


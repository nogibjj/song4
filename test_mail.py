import requests
import os, json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CONFIG_SECRET_DIR = os.path.join(BASE_DIR, ".config_secret")
CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, "setting_local.json")
config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())


def send_simple_message(email_address):
    print("send message to {0}".format(email_address))
    return requests.post(
        "https://api.mailgun.net/v3/project4.org/messages",
        auth=("api", str(config_secret_common["email_api_key"])),
        data={
            "from": "Happy User <mailgun@project4.org>",
            "to": [email_address],
            "subject": "Hello",
            "text": "Testing!",
        },
    )


send_simple_message("song.oh@outlook.com")


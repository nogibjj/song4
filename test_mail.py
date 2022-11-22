import requests


def send_simple_message(email_address):
    print("send message to {0}".format(email_address))
    return requests.post(
        "https://api.mailgun.net/v3/sandbox29c908f3254f4533828f37625ca9b30d.mailgun.org/messages",
        auth=("api", "0784009ad8cb3957058ad22b401cf260-69210cfc-0a11600c"),
        data={
            "from": "Happy User <mailgun@sandbox29c908f3254f4533828f37625ca9b30d.mailgun.org>",
            "to": [email_address],
            "subject": "Hello",
            "text": "Testing some Mailgun awesomness!",
        },
    )


send_simple_message("song.oh@outlook.com")


import requests
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxbc291829653647869a2d4b921ede76b1.mailgun.org/messages",
        auth=("api", "6c1ef20602d0090f9e79e3a968a518b0-102c75d8-0d6550e1"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxbc291829653647869a2d4b921ede76b1.mailgun.org>",
              "to": "Om Patil <ompatil16022002@gmail.com>",
              "subject": "Hello Om Patil",
              "text": "Congratulations Om Patil, you just sent an email with Mailgun!  You are truly awesome!"})

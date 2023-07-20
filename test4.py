from mailjet_rest import Client
import os
api_key = '88fed663b7c741a97516e01fc4c5b5fe'
api_secret = 'a9b79ba4ca707a6e5d8def3e05474d19'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "ompatil16022002@gmail.com",
        "Name": "ANfninq"
      },
      "To": [
        {
          "Email": "ompatil16022002@gmail.com",
          "Name": "ANfninq"
        }
      ],
      "Subject": "Greetings from Mailjet.",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())
print("Mail Sent Successfully")
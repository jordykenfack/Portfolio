import smtplib
import ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    user_name = "jordykenfack@gmail.com"
    password = os.getenv("PASSWORD")
    message = """\
subject:Greetings!

How are you ?"""
    receiver_email = "jordykenfack@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver_email, message)



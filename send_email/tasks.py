from celery import shared_task
import smtplib
from email.mime.text import MIMEText
from send_email.models import SendEmail


@shared_task
def send_email(message):
    sender = SendEmail.objects.get()
    # password = os.getenv("")
    password = 'jppemvgwasrwhkhh'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Click"
        server.sendmail(sender, sender, msg.as_string())

        return "Succes!"

    except Exception as _ex:
        return f"{_ex}\nCheck your login or pass please"


# def main():
#     message = input("Input: ")
#     print(send_email(message=message))
#
#
# if __name__ == "__main__":
#     main()

# jppemvgwasrwhkhh


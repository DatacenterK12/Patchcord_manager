import os
import smtplib

from dotenv import load_dotenv

load_dotenv()

DATA = {
    "smtp_server": os.getenv("SMTP_SERVER"),
    "email_fl": os.getenv("EMAIL_FL"),
    "email_noc": os.getenv("EMAIL_NOC"),
    "password": os.getenv("PASSWORD"),
}

smpObj = smtplib.SMTP(
    DATA["smtp_server"],
    587,
)
smpObj.starttls()
smpObj.login(DATA["email_fl"], DATA["password"])


def send_mail(cross, length):
    SUBJECT = "STOCKS ARE LOW"
    TEXT = f"You don't have enough {cross} {length}m cables left"
    message = "Subject: {}\n\n{}".format(SUBJECT, TEXT)
    print(message)
    smpObj.sendmail(
        DATA["email_fl"],
        DATA["email_noc"],
        message,
    )


def main():
    cross = "SC-SC"
    length = "20M"
    send_mail(cross, length)


if __name__ == "__main__":
    main()

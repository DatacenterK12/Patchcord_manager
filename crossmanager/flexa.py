import smtplib

smpObj = smtplib.SMTP(
    "mail.nic.ru",
    587,
)
smpObj.starttls()
smpObj.login("flexa@k12.spb.ru", "RG8tku95")


def send_mail(cross, length):
    SUBJECT = "STOCKS ARE LOW"
    TEXT = f"You don't have enough {cross} {length}m cables left"
    message = "Subject: {}\n\n{}".format(SUBJECT, TEXT)
    print(message)
    smpObj.sendmail(
        "flexa@k12.spb.ru",
        "noc@k12.spb.ru",
        message,
    )


def main():
    cross = "SC-SC"
    length = "20M"
    send_mail(cross, length)


if __name__ == "__main__":
    main()

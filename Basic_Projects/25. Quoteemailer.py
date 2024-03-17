import smtplib
import datetime as dt
import random

smtp_port = 587
smtp_server = "smtp.gmail.com"
my_email = "vyomdummy123@gmail.com"
to_email = "vyomshah1401@gmail.com"
password = "kexndlggwymjmaoq"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("C:/Users/vyoms/Downloads/quotes.csv") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    try:
        # print("Connecting to server")
        connection = smtplib.SMTP(smtp_server, smtp_port)
        connection.starttls()
        connection.login(my_email, password)
        # print("Connected to server:- ")
        # print()
        print(f"Sending mail to : {to_email}")
        subject = f"Subject: Monday Motivation\n\n {quote}"
        subject_bytes = subject.encode("utf-8")
        connection.sendmail(my_email, to_email, msg=subject_bytes)
        print(f"Mail sent to : {to_email}")

    except Exception as e:
        print(e)

    finally:
        connection.close()

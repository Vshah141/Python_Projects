#CHECK STARRED MESSGAE FOR REFERENCE IN GOOGLE

import smtplib
import ssl

smtp_port=587
smtp_server="smtp.gmail.com"

message="Great work"
my_email="vyomdummy123@gmail.com"
to_email="krunalmgohel@gmail.com"
password="kexndlggwymjmaoq"

simple_email_context=ssl.create_default_context()

try:
    print("Connecting to server")
    connection=smtplib.SMTP(smtp_server,smtp_port)
    connection.starttls(context=simple_email_context)
    connection.login(my_email,password)
    print("Connected to server:- ")
    print()
    print(f"Sending mail to : {to_email}")
    connection.sendmail(my_email,to_email,message)
    print(f"Mail sent to : {to_email}")

except Exception as e:
    print(e)

finally:
    connection.close()






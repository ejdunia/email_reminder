import smtplib
import os
import time
from datetime import datetime, date
from email.message import EmailMessage
# importing all necessary modules to be used

email_add = os.environ.get('MY_EMAIL')
email_pass = os.environ.get('EMAIL_PASS')
# have already had set os.environ files 


print(f"Hi! this is a program that sends an email to you every hour reminding you to drink water.\nWater is LIFE!!!"
        "\nYour username will be the first part of your email")

user_email = input("Enter your email address: ")
username = user_email.split('@')[0]
now = datetime.now()
print(now.strftime("%H:%M:%S"))

while True:
    message = f"Hi! {username},\nThe time is {datetime.now().time()}, please take your water as recommended by the doctor.\nTodays Date: {date.today()} "
    # msg = EmailMessage()
    # msg['Subject'] = 'Python class test mail'
    # msg['From'] = email_add
    # msg['To'] = user_email0
    # msg.set_content(message)
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #     smtp.login(email_add, email_pass)
    #     smtp.send_message(msg)
    print(message)
    time.sleep(60) # the arg is in seconds so 60 secs 


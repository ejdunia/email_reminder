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

def get_freq():
    while True:
        try:
            freq = int(input('Enter the frequency(in minutes) you want to be reminded: '))
        except ValueError:
            continue
        return freq


def send_message(subject, message, email, email_add=email_add, e_mesg=EmailMessage()):
    """function to send the mail with  """
    msg = e_mesg
    msg['Subject'] = subject
    msg['From'] = email_add
    msg['To'] = email
    msg.set_content(message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_add, email_pass)
        smtp.send_message(msg)

user_email = input("Enter your email address: ")
freq = get_freq()

username = user_email.split('@')[0]
now = datetime.now()

while True:
    message = f"Hi! {username},\nThe time is {datetime.now().time()}, please take your water as recommended by the doctor.\nTodays Date: {date.today()} "
    send_message(e_mesg=EmailMessage(), subject="Water Reminder", email_add=email_add, email=user_email, message=message)
    print(message)
    time.sleep(60 * freq) # the arg is in seconds so 60 secs 


"""
twilio
datetime module 
time

Step 1: twilio client setup
Step 2: User Input Say Whattsapp number , Date and time and Message to be sent 
Step 3: Scheduling Logic

"""

from twilio.rest import Client
from datetime import datetime,timedelta
import time

# Step2 
from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_whatsapp = os.getenv("FROM_WHATSAPP")

client = Client(account_sid,auth_token)


def send_Whattsapp_message(recipient_number,message_body):
    try:
        message = client.messages.create(
            from_=from_whatsapp,
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message Sent Successfully ! Message SID{message.sid}')
    except Exception as e :
        print("An Error occured while sending Message")


# Step to take input from user 
name = input("Enter the receipient Name : ")
number = input("Enter the receipient whattsapp number with Country code : ")
message_body =input(f"Enter the message you want to send to the{name}")

date_str = input("Enter the date to send the whattsapp message (YYYY -MM -DD) :")
time_str = input("Enter the time to send the message (HH :MM in 24 hours format) : ")


# date time 
scheduled_datetime = datetime.strptime(f'{date_str} {time_str}','%Y-%m-%d  %H:%M')
current_datetime = datetime.now()


# Calculate the delay 

time_difference = scheduled_datetime - current_datetime
delay_seconds = time_difference .total_seconds ()

if delay_seconds <= 0 :
    print("The specified time is in the past . Please give the correct time ")
else:
    print(f"Message scheduled to be sent to {name} at {scheduled_datetime}.")

    time.sleep(delay_seconds)

    # send the message
    send_Whattsapp_message(number,message_body)
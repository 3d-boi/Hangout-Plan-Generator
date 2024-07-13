import random
import datetime
import os
import dotenv
import email.message
import smtplib

location_list = ['School', 'Ahl-Misr Garden', 'Future Mall']
will_generate = True#bool(random.getrandbits(1))

dotenv.load_dotenv('.env')

def generate_plan():
    location = random.choice(location_list)
    time = datetime.time(random.randint(6,9),00).strftime('%H:%M')
    email_msg = f"""
    Greetings, Esteemed Member,

    The time has come to gather once more. You are cordially invited to an exclusive SSS hangout.
    Expect the unexpected and prepare for an evening of intrigue and camaraderie.

    Details are shrouded in secrecy, but rest assured, your presence is crucial.

    Time: {time} PM
    Location: The {location}

    Respond with discretion.

    In shadows and secrecy,

    ~The SSS Planning Department~
    """
    send_email(email_msg)

def send_email(message:str):
    sender_email = str(os.environ.get('SENDER_EMAIL'))
    email_passkey = str(os.environ.get('EMAIL_PASSKEY'))
    recipient_emails = [str(os.environ.get('RECIPIENT_EMAILS'))]
    
    mail = email.message.Message()
    mail['Subject'] = "SSS Hangout Invitation"
    mail.set_payload(message)
    mail_str = mail.as_string()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        # Login to the sender's email account
        server.login(sender_email, email_passkey)
        # Send email
        server.sendmail(sender_email,recipient_emails,mail_str.encode('utf-8'))
    
    print('mail sent!')

if (will_generate):
    #generate a plan
    plan = generate_plan()
else:
    #End the program
    print("No hangout")
    pass

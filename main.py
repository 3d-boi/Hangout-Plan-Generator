import random
import datetime
import os
import dotenv
import email.message
import smtplib

location_list = ['School', 'Ahl-Misr Garden', 'Future Mall']
will_generate = bool(random.getrandbits(1))

dotenv.load_dotenv('.env')

def generate_plan():
    location = random.choice(location_list)
    time = datetime.time(random.randint(6,9),00).strftime('%H:%M')
    email_subject = 'SSS Hangout Invitation'
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
    send_email(email_msg,email_subject)

def initiate_members():
    email_subject = 'Exciting News: Introducing the SSS Planning Department'
    email_msg = """
    Greetings, Esteemed Members,

    We are thrilled to announce the formation of the new Planning Department within the Secret Shit Society (SSS).
    This elite team of master strategists is dedicated to crafting ingenious and thrilling plans for our society's future activities.

    Expect more details about upcoming hangouts and events to be revealed soon. Prepare for a series of unforgettable experiences and adventures!

    Stay tuned and keep your calendars flexible.

    In shadows and secrecy,

    ~The SSS Planning Department~
    """
    send_email(email_msg,email_subject)

def send_email(message:str,subject:str):
    sender_email = str(os.environ.get('SENDER_EMAIL'))
    email_passkey = str(os.environ.get('EMAIL_PASSKEY'))
    recipient_email1 = [str(os.environ.get('RECIPIENT_EMAIL1'))]
    recipient_email2 = [str(os.environ.get('RECIPIENT_EMAIL2'))]
    recipient_email3 = [str(os.environ.get('RECIPIENT_EMAIL3'))]
    
    mail = email.message.Message()
    mail['Subject'] = subject
    mail.set_payload(message)
    mail_str = mail.as_string()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        # Login to the sender's email account
        server.login(sender_email, email_passkey)
        # Send email
        server.sendmail(sender_email,recipient_email1,mail_str.encode('utf-8'))
        server.sendmail(sender_email,recipient_email2,mail_str.encode('utf-8'))
        server.sendmail(sender_email,recipient_email3,mail_str.encode('utf-8'))
    
    print('mail sent!')

if (will_generate):
    #generate a plan
    plan = generate_plan()
else:
    #End the program
    print("No hangout")
    pass

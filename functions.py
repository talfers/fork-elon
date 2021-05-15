import smtplib, ssl
from functions import *
from keys import *

# look for terms in tweet
def find_terms(terms, text):
    found = False
    for term in terms:
        if term in text:
            found = True
    return found


def send_alert(subject, body):
    context = ssl.create_default_context()
    message = 'Subject: {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, smtp_key)
        server.sendmail(sender_email, receiver_email, message)

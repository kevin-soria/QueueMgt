from twilio.rest import Client
import os
from models import Queue

Q = Queue ()

def first_function(mess):

    account_sid = os.environ.get('SID_KEV') 
    auth_token = os.environ.get('TOKEN_KEV')
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="Hi "+ ", your number:" + Q.number[0] +"in line.",
            from_='+12064660790',
            to=Q.number[0]
        )

    print(message.sid)
    return repr(Q._queue[0])
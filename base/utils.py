import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(_from, subject, body) -> bool:
    _to = "niteric@gmail.com"
    str_to = ''.join(_to)
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = _from
    message["To"] = str_to

    # Turn these into plain/html MIMEText objects
    part = MIMEText(body, "html")
    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part)
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        # print(message.as_string())
        server.login(_to, "zkzmoereafzcvfhd")
        if server.sendmail(f"{_from}", f"{str_to}", f"{message.as_string()}"):
            return True
        else:
            return False


# if send_email("erickmaina29@student.ku.ac.ke", "hello", "hello2"):
#     print("message sent")
# else:
#     print("message not sent")

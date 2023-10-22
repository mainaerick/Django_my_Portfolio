from email.mime.text import MIMEText
from django.core.mail import send_mail
from requests import Response

from Django_Portfolio.settings import DEFAULT_FROM_EMAIL


def send_email(_from, subject, body):

    try:
        subject = subject
        # name = data["name"]
        # email = data["email"]
        message = body
        from_email = _from
        recipient_list = [DEFAULT_FROM_EMAIL]

        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        # enquiry = Enquiry(name=name, email=email, subject=subject, message=message)
        # enquiry.save()

        return Response({"success": "Your Enquiry was successfully submitted"})

    except:
        return Response({"fail": "Enquiry was not sent. Please try again"})


# def send_email(_from, subject, body) -> bool:
#     _to = "niteric@gmail.com"
#     str_to = ''.join(_to)
#     message = MIMEMultipart("alternative")
#     message["Subject"] = subject
#     message["From"] = _from
#     message["To"] = str_to

#     # Turn these into plain/html MIMEText objects
#     part = MIMEText(body, "html")
#     # Add HTML/plain-text parts to MIMEMultipart message
#     message.attach(part)
#     # Create secure connection with server and send email
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#         # print(message.as_string())
#         server.login(_to, "zkzmoereafzcvfhd")
#         if server.sendmail(f"{_from}", f"{str_to}", f"{message.as_string()}"):
#             return True
#         else:
#             return False


# if send_email("erickmaina29@student.ku.ac.ke", "hello", "hello2"):
#     print("message sent")
# else:
#     print("message not sent")

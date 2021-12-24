from django.shortcuts import render
from base.forms import MessageForm
from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail
from base.models import About, Experience, Message, Project, Skill, Tool
from base.utils import send_email
# Create your views here.


def home(request):

    about = About.objects.all().first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    tools = Tool.objects.all()
    context = {"about": about, "projects": projects,
               "skills": skills, "experiences": experiences, "tools": tools}
    form = MessageForm()
    if request.method == 'POST':
        # if form.is_valid():
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('msg')
        Message.objects.create(name=name, email=email, message=message)
        subject = f"{name} sent you a portfolio message."
        recipient_list = ["niteric@gmail.com", ]
        # send_mail(subject, message, email, recipient_list)
        if send_mail(subject, message, email, recipient_list):
            print("message sent")
            messages.success(
                request, "Message sent successfully.")
        else:
            print("message not sent")
            messages.error(
                request, "An error occured message could not be sent.")

        # else:
        #     print("form not valid")
        #     messages.error(
        #         request, "An error occured message could not be sent.")
    return render(request, 'home.html', context)

from django.shortcuts import render
from django.core.mail import send_mail
import logging


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def mygames(request):
    return render(request, 'mygames.html')

def gallery(request):
    
    return render(request, 'gallery.html')

def contact(request):
    logger = logging.getLogger(__name__)
    if request.method == "POST":
        message_name = request.POST['firstname']
        message_email = request.POST['mail']
        message_message = request.POST['message']
        print("msggg" + message_message)
        logger.warning("Platform isk")
        send_mail(
            "Message from: " + message_name,
            message_message + "\n" + message_email,
            message_email,
            ["se.batuhan.uysal@gmail.com"],
        )

        return render(request, 'contact.html', {"message_name": message_name})
    else:
        return render(request, "contact.html", {})

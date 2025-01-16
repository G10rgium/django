from django.shortcuts import render
from django.conf import settings
from .models import Customer
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.



def index(request):
    if request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")
        subject = request.POST.get("subject")
        send_mail(subject, message, from_email=settings.EMAIL_HOST_USER, recipient_list=[email])
    return render(request, "index.html")



def about(request):
    return render(request, "about.html")



def donald(request):

    return render(request, "donald.html")



def wendy(request):
    return render(request, "wendy.html")



def shawarma(request):
    return render(request, "shawarma.html")



def tsisqvili(request):
    return render(request, "tsisqvili.html")



def kfc(request):
    return render(request, "kfc.html")



def dunkin(request):
    return render(request, "dunkin.html")



def log_in(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")


    return render(request, "log_in.html")



def reg(request):
    return render(request, "reg.html")


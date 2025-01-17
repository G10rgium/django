from django.shortcuts import render, redirect
from django.conf import settings
from .models import Customer
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout



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


def reg(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request, "es emaili arsebobs")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "username arsebobs ukve")
            else:
                consumer = User(username= username, email=email)
                consumer.set_password(password)
                consumer.save()
                messages.info(request, "user registered")
    return render(request, "reg.html")



def log_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "":
            messages.info(request, "username ar aris shemoyvanili")
        elif password == "":
            messages.info(request, "paroli ar aris shemoyvanili")
        else:
            log = auth.authenticate(username=username, password=password)
            print(log)
            if log is not None:
                auth.login(request, log)
                return redirect("index")
            # else:
            #     auth.logout(request)
            #     return redirect("index")
    return render(request, "log_in.html")

# def log_out(request):



def cart(request):
    return render(request, "cart.html")
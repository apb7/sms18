from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "sms_auth/home.html")


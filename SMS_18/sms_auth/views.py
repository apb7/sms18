from django.shortcuts import render
from django.http import HttpResponse

def form(request):
    return render(request, "sms_auth/home.html")

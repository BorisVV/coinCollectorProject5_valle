from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "coins_web_app/home.html")

def displayInfo(request):
    return render(request, "coins_web_app/basic.html", {'displayInfo': ['for this I can say that','and that is all I have to say']})

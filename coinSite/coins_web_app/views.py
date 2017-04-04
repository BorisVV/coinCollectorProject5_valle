from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "coins_web_app/home.html")

def displayInfo(request):
    return render(request, "coins_web_app/basic.html", {'displayInfo': ['This is an example on how to display info in the same page']})

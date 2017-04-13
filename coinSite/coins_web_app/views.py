from django.shortcuts import render, redirect, reverse, get_list_or_404
from django.conf.urls import url
from django.http import HttpResponse
from .models import DisplayQuaters
from .forms import NewQuatersForm

def quarters_list(request):

    # If a POST request.
    if request.method == 'POST':
        form = NewQuatersForm(request.POST)
        newQuater = form.save()
        if form.is_valid():
            newQuater.save()
            return redirect('coins_web_app/basic.html')

    # If not a POST request.
    quaters = DisplayQuaters.objects #.filter(orderby=number)
    form = NewQuatersForm()
    return render(request, 'coins_web_app/basic.html', {'quarters' : quaters, 'form' : form})

# def index(request):
#     return render(request, "coins_web_app/basic.html")

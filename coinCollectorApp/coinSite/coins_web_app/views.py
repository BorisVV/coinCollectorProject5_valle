from django.shortcuts import render, redirect, reverse, get_list_or_404
from django.conf.urls import url
from django.http import HttpResponse
from .models import DisplayQuarters
from .forms import NewQuartersForm

def index(request):
    return render(request, "coins_web_app/quarters_list.html")


def quarters_list(request):

    # If a POST request.
    if request.method == 'POST':
        form = NewQuartersForm(request.POST)
        newQuarter = form.save()
        if form.is_valid():
            newQuarter.save()
            return redirect('coins_web_app/basic.html')

    # If not a POST request.
    quarters = DisplayQuarters.objects.all() #.filter(orderby=number)
    form = NewQuartersForm()
    return render(request, 'coins_web_app/basic.html', {'quarters_list' : quarters, 'form' : form})

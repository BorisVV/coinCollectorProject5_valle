from django.shortcuts import render, redirect, reverse, get_list_or_404
from django.conf.urls import url
from django.http import HttpResponse
from .models import DisplayQuarters
from .forms import NewQuartersForm

def home(request):
    return render(request, "coins_web_app/base.html")


def quarters_list(request):

    # If a POST request.
    if request.method == 'POST':
        form = NewQuartersForm(request.POST)
        newQuarter = form.save()
        if form.is_valid():
            newQuarter.save()
            return redirect('coins_web_app/quartersTable.html')

    # If not a POST request.
    quarters = DisplayQuarters.objects.all() #.filter(orderby=number)
    form = NewQuartersForm()
    return render(request, 'coins_web_app/quartersTable.html', {'quarters_list' : quarters, 'form' : form})



# def create_account(request):
#     # function to allow a user to create their own account
#     if request.method == 'POST':
#         # sets a new user and gives them a username
#         new_user = User(username = request.POST["username"],
#                     email=request.POST["email"],
#                     first_name=request.POST["first_name"],
#                     last_name=request.POST["last_name"],
#                     age=request.POST["age"],
#                     # city=request.POST["city"],
#                     # state=request.POST["state"]
#                     )
#
#         # sets an encrypted password
#         new_user.set_password(request.POST["password"])
#         new_user.save()
#         # adds the new user to the database
#         Person.objects.create(user=new_user,
#                           first_name=str(request.POST.get("first_name")),
#                           last_name=str(request.POST.get("last_name")),
#                           email=str(request.POST.get("email")),
#                           age=str(request.POST.get("age")),
#                         #   city=str(request.POST.get("city")),
#                         #   state=str(request.POST.get("state"))
#                           )
#         new_user.is_active = True
#         new_user.save()
#         return redirect('../')
#     else:
#         return render(request, 'folerName/create_account.html')

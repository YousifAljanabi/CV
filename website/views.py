from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse

from django.db import IntegrityError


def index(request):
    return render(request, "website/index.html",)


def login(request):
    # if request.method == "POST":

    #     # Attempt to sign user in
    #     username = request.POST["username"]
    #     password = request.POST["password"]
    #     user = authenticate(request, username=username, password=password)

    #     # Check if authentication successful
    #     if user is not None:
    #         login(request, user)
    #         return HttpResponseRedirect(reverse("index"))
    #     else:
    #         return render(request, "network/login.html", {
    #             "message": "Invalid username and/or password."
    #         })
    # else:
        return render(request, "website/login.html",)
    


def signup(request):
    return render(request, "website/signup-type-select.html",)


def createSeeker(request):
    if request.method == "GET":

        return render(request, "website/signup.html",{
         "type" : "seeker"
        })

def createEmployer(request):
    return render(request, "website/signup.html",{
        "type" : "employer"
    })


def createAccount(request):
    # if request.method == "POST":
    #     username = request.POST["username"]
    #     email = request.POST["email"]
    #     # name = request.POST["name"]
    #     # phone = request.POST["phone"]
    #     # Ensure password matches confirmation
    #     password = request.POST["password"]
    #     confirmation = request.POST["confirmation"]
    #     if password != confirmation:
    #         return render(request, "website/signup.html", {
    #             "message": "Passwords must match."
    #         })

    #     # Attempt to create new user
    #     try:
    #         user = User.objects.create_user(username, email, password)
    #         user.save()
    #     except IntegrityError:
    #         return render(request, "website/signup.html", {
    #             "message": "Username already taken."
    #         })
    #     login(request, user)
    #     return HttpResponseRedirect(reverse("index"))
    # else:
        return render(request, "website/signup.html")



def jobDetails(request):
    return render(request, "website/job.html")


def companyProfile(request):
    return render(request, "website/company_profile.html")
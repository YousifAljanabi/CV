from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse

from django.db import IntegrityError

from .models import User
from .api import UserTypeApi

SIGNUP_PAGE = "website/signup.html"


def index(request):
    return render(request, "website/landing_page.html")


def create_seeker(request):
    if request.method == "GET":
        return render(request, SIGNUP_PAGE, {
            "type": "seeker"
        })


def create_employer(request):
    return render(request, SIGNUP_PAGE, {
        "type": "employer"
    })


def user_login(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            user_type = user.user_type
            login(request, user)
            if user_login(request):
                pass
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "website/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "website/login.html", )


def signup(request):
    return render(request, "website/signup-type-select.html", )




def create_account(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # name = request.POST["name"]
        # phone = request.POST["phone"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        user_type_name = request.POST["type"]

        user_type = UserTypeApi.get_by_name(user_type_name)

        if user_type is None:
            return render(request, SIGNUP_PAGE, {
                "message": "Invalid User Type."
            })

        if user_type.id == 1:
            return render(request, SIGNUP_PAGE, {
                "message": "Invalid User Type."
            })

        if password != confirmation:
            return render(request, SIGNUP_PAGE, {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.user_type = user_type
            user.save()
        except IntegrityError:
            return render(request, SIGNUP_PAGE, {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, SIGNUP_PAGE)


def job_details(request):
    return render(request, "website/job.html")

def companyProfile(request):
    return render(request, "website/company_profile.html")


def job_search(request):
    return render(request, "website/job_search.html")

def user_profile(request):
    return render(request, "website/user_profile.html")

def jobs_list(request):
    return render(request, "website/jobs_list.html")

def employee_list(request):
    return render(request, "website/employee_list.html")
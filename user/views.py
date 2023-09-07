from django.shortcuts import render, redirect
from user.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        User.objects.create_user(username=username, email=email, password=password)
        return redirect("/todo/")
    elif request.method == "GET":
        return render(request, "user/signup.html")
    else:
        return HttpResponse("invalid request method!!", status=405)


def log_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/todo/")
        else:
            return HttpResponse("invalid auth!!", status=401)
    elif request.method == "GET":
        return render(request, "user/login.html")
    else:
        return HttpResponse("invalid request method!!", status=405)


def log_out(request):
    if request.method == "POST":
        logout(request)
        return redirect("/todo/")
    else:
        return HttpResponse("invalid request method!!", status=405)
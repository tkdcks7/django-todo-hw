from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo.models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    pass

@login_required(login_url="/user/login/")
@csrf_exempt
def create(request):
    if request.method == "POST":
        Todo.objects.create(
            title=request.POST["title"],
            content=request.POST["content"], 
            user=request.user,
            image=request.FILES.get("image"),
        )
        return redirect("/todo/")
    elif request.method == "GET":
        return render(request, "todo/create.html")
    else:
        return HttpResponse("invalid request method!!", status=405)


def read(request):
    pass


def update(request):
    pass


def delete(request):
    pass
from django.contrib.auth import login
from django.shortcuts import Http404, redirect, render
from django.urls import reverse

from django_users.forms import NewUserCreationForm

# Create your views here.


def dashboard(request):
    return render(request, "dashboard.html", {})


def register(request):
    if request.method == "GET":
        return render(request, "register.html", {"form": NewUserCreationForm})
    elif request.method == "POST":
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            return Http404("Invalid Form")

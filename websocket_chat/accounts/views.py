from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


def register(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == "POST":
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user: User = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data["password1"])
            new_user.save()

            login(request, new_user)
            return redirect("/")

    else:
        user_register_form = UserRegisterForm(data=request.POST)

    return render(request, "accounts/register.html", {"form": user_register_form})

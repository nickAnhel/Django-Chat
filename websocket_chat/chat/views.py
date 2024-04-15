from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import Chat


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "chat/home.html")


def chat_detail(requst: HttpRequest, chat_id: int) -> HttpResponse | HttpResponseRedirect :
    try:
        chat: Chat = requst.user.chats_joined.get(pk=chat_id)  # type: ignore
    except Chat.DoesNotExist:
        return redirect("/")
    return render(requst, "chat/detail.html", {"chat": chat})

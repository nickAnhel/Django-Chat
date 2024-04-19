from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Chat


def chat_list(request: HttpRequest) -> HttpResponse:
    chats = Chat.objects.all()
    return render(request, "chat/list.html", {"chats": chats})


def chat_detail(requst: HttpRequest, chat_id: int) -> HttpResponse | HttpResponseRedirect:
    chat: Chat = get_object_or_404(Chat, pk=chat_id)
    return render(requst, "chat/detail.html", {"chat": chat})


def chat_join(request: HttpRequest, chat_id: int) -> HttpResponseRedirect:
    chat: Chat = get_object_or_404(Chat, pk=chat_id)
    chat.members.add(request.user)
    return HttpResponseRedirect(reverse("chat:detail", kwargs={"chat_id": chat_id}))

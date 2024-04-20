from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

from .models import Chat
from .forms import ChatCreateForm, ChatSearchForm


def chat_list(request: HttpRequest) -> HttpResponse:
    chats = Chat.objects.all()

    if request.method == "POST":
        chat_search_form = ChatSearchForm(data=request.POST)
        if chat_search_form.is_valid():
            chats = chats.filter(title__icontains=chat_search_form.cleaned_data["query"])
    else:
        chat_search_form = ChatSearchForm()

    return render(request, "chat/list.html", {"chats": chats, "search_form": chat_search_form})


@login_required
def chat_detail(requst: HttpRequest, chat_id: int) -> HttpResponse | HttpResponseRedirect:
    chat: Chat = get_object_or_404(Chat, pk=chat_id)
    return render(requst, "chat/detail.html", {"chat": chat})


@login_required
def chat_join(request: HttpRequest, chat_id: int) -> HttpResponseRedirect:
    chat: Chat = get_object_or_404(Chat, pk=chat_id)
    chat.members.add(request.user)
    return HttpResponseRedirect(reverse("chat:detail", kwargs={"chat_id": chat_id}))


@login_required
def chat_create(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == "POST":
        chat_create_form = ChatCreateForm(data=request.POST)
        if chat_create_form.is_valid():
            new_chat = chat_create_form.save(commit=False)
            new_chat.slug = slugify(new_chat.title)
            new_chat.owner = request.user
            new_chat.save()
            new_chat.members.add(request.user)

            return redirect(reverse("chat:detail", kwargs={"chat_id": new_chat.id}))
    else:
        chat_create_form = ChatCreateForm()

    return render(request, "chat/create.html", {"form": chat_create_form})

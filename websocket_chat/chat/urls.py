from django.urls import path
from . import views


app_name = "chat"


urlpatterns = [
    path("", views.chat_list, name="list"),
    path("search/", views.chat_list, name="search"),
    path("chat/<int:chat_id>/", views.chat_detail, name="detail"),
    path("chat/<int:chat_id>/join/", views.chat_join, name="join"),
    path("chat/create/", views.chat_create, name="create"),
]

from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("chat/<int:chat_id>/", views.chat_detail, name="detail"),
]

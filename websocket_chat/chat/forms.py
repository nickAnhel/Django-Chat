from django import forms

from .models import Chat


class ChatCreateForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ["title"]

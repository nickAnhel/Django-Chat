from django import forms

from .models import Chat


class ChatCreateForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ["title"]


class ChatSearchForm(forms.Form):
    query = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Search"}), label=False)

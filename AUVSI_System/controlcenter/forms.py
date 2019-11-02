from django import forms
from django.db import models
from .models import InteropServer


class InteropServerForm(forms.ModelForm):
    class Meta:
        model = InteropServer
        fields = ('url', 'username', 'password')
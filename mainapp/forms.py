from django.forms import ModelForm
from django.forms import forms

from .models import Streamer

class StreamerForm(ModelForm):
    class Meta:
        model = Streamer
        fields = ("__all__")

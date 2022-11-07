from django.forms import ModelForm

from .models import Streamer

class StreamerForm(ModelForm):
    class Meta:
        model = Streamer
        fields = ("__all__")
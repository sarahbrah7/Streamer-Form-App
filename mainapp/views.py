from django.shortcuts import render
# from django.forms import model_to_dict
from django.http import HttpResponse, HttpRequest, JsonResponse

from mainapp.models import Streamer

def index(request: HttpRequest) -> HttpResponse:
    title = "My Cool Streamer App"
    return render(request, "mainapp/index.html", {
        'title': title,
        'n': Streamer.objects.all().count(),
    })

def streamers_api(request):
    if request.method == 'GET':
        return JsonResponse({
            'streamers': [
                streamer.to_dict() for streamer in Streamer.objects.all()
            ]
        })
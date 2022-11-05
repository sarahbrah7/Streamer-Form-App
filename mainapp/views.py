from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

from mainapp.models import Streamer

def index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse(f"Hello world, at the moment there are {n} streamers")
    return render(request, "mainapp/index.html", {
        'n': Streamer.objects.all().count()
    })

def streamers_api(request):
    JsonResponse({
        'streamers': [
            streamer.to_dict()
            for streamer in Streamer.object.all()
        ]
    })
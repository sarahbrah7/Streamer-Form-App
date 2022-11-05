from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from mainapp.models import Streamer

def index(request: HttpRequest) -> HttpResponse:
    n = Streamer.objects.all().count()
    # return HttpResponse(f"Hello world, at the moment there are {n} streamers")
    title = "My cool food app"
    return render(request, "mainapp/index.html", {
        'title': title,
        'n': f(n)
    })

def f(n: int) -> int:
    return n + 1
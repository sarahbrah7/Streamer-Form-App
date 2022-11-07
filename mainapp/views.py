from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.forms.models import model_to_dict

import json
from django.views.decorators.csrf import csrf_exempt
from mainapp.models import Streamer
from mainapp.forms import StreamerForm

def index(request: HttpRequest) -> HttpResponse:
    title = "My cool food app"
    return render(request, "mainapp/index.html", {
        'title': title,
        'n': Streamer.objects.all().count()
    })
@csrf_exempt
def streamers_api(request: HttpRequest) -> HttpResponse:
    form = StreamerForm()
    #this is the GET method
    if request.method == 'GET':
        return JsonResponse({
            'streamers': [
                streamer.to_dict() for streamer in Streamer.objects.all()
            ]
        })
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        client = Streamer.objects.create(
            streamer_name = data['streamer_name'],
            platform = data['platform'],
            last_stream = data['last_stream'],
            rating = data['rating'],
        )
        client.save()
        return JsonResponse({
            'data': [data['streamer_name']]
        })

def streamer_api(request: HttpRequest, streamer_id: int) -> HttpResponse:
    streamer = get_object_or_404(Streamer, id=streamer_id)

    if request.method == 'GET':
        return JsonResponse(streamer.to_dict())

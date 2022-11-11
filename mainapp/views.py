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
    #This is the GET method
    if request.method == 'GET':
        return JsonResponse({
            'streamers': [
                streamer.to_dict() for streamer in Streamer.objects.all()
            ]
        })
    #This is the POST method
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
            'data': [data]
        })
    #This is the PUT method
    if request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        client = Streamer.objects.get(id = data['streamer_id'])
        client.platform = data['platform'] #Updates the platform 
        client.save()
        return JsonResponse({
            'Streamer': [data]
        })
    #This is the DELETE method
    if request.method == 'DELETE':
        data = json.loads(request.body.decode('utf-8'))
        Streamer.objects.get(id = data['streamer_id']).delete() #Deletes the selected data based on id
        return JsonResponse({
            'Streamer': [data]
        })
        
def streamer_api(request: HttpRequest, streamer_id: int) -> HttpResponse:
    streamer = get_object_or_404(Streamer, id=streamer_id)

    if request.method == 'GET':
        return JsonResponse(streamer.to_dict())

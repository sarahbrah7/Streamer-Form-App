from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseRedirect

from mainapp.models import Streamer
from mainapp.forms import StreamerForm

def index(request: HttpRequest) -> HttpResponse:
    title = "My cool food app"
    return render(request, "mainapp/index.html", {
        'title': title,
        'n': Streamer.objects.all().count()
    })

def streamers_api(request: HttpRequest) -> HttpResponse:
    #this is the GET method
    if request.method == 'GET':
        return JsonResponse({
            'streamers': [
                streamer.to_dict() for streamer in Streamer.objects.all()
            ]
        })
    if request.method == 'POST':
    #     # need to create a new recipe
    #     form = StreamerForm(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect('/thanks/')
    #     else:
    #         form = ContactForm()

    #     # return the new recipe as JSON
    #     streamer = Streamer.objects.create()
    #     return JsonResponse({
    #         'streamer': [
    #             streamer.to_dict
    #         ]
    #     })
        pass

def streamer_api(request: HttpRequest, streamer_id: int) -> HttpResponse:
    streamer = get_object_or_404(Streamer, id=streamer_id)

    if request.method == 'GET':
        return JsonResponse(streamer.to_dict())

from django.contrib import admin
from django.urls import path

from mainapp.views import index, streamers_api, streamer_api

# creates url patterns and calls for the api to get 
# database information on streamers
urlpatterns = [
    path('', index),
    path('api/streamers', streamers_api),
    path('api/streamers/<int:streamer_id>', streamer_api, name="streamer api"),
]

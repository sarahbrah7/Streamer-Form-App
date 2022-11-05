from django.db import models

class Streamer(models.Model):
    streamer_name = models.CharField(max_length=200)
    platform = models.BooleanField(verbose_name = "streamed on twitch?", default = False)
    last_stream = models.DateTimeField('last watched stream')
    rating = models.FloatField(default = 0.0)

    def __str__(self):
        return self.streamer_name

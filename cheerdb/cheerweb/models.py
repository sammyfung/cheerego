from django.db import models

class CheerBoard(models.Model):
  scraptime = models.DateTimeField()
  posttime = models.DateTimeField()
  poster = models.CharField(max_length=16)
  message = models.TextField()


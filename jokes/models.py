from django.db import models


# Create your models here.
class Joke(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()


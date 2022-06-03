from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import false


class Note(models.Model):
    title   = models.CharField(max_length=200)
    content = models.TextField(null=True)
    user    = models.ForeignKey(User, on_delete=models.CASCADE, null=false)

class Favoritos(models.Model):
    id_card   = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=false)

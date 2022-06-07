from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import false, true

class Note(models.Model):
    title    = models.CharField(max_length=200)
    content  = models.TextField(null=True)
    photo    = models.FileField(upload_to='imagens', null=true)
    time     = models.FloatField(null=true)
    username = models.TextField(null=true)
    user     = models.ForeignKey(User, on_delete=models.CASCADE, null=false)

    def delete(self, using=None, keep_parents=False):
        self.photo.storage.delete(self.photo.name)
        super().delete()

class Favoritos(models.Model):
    id_card   = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=false)

from rest_framework import serializers
from .models import Note, Favoritos


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content']

class FavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = ['id_card', 'user']
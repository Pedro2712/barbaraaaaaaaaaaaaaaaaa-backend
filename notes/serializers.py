from rest_framework import serializers
from .models import Note, Favoritos


class NoteSerializer(serializers.ModelSerializer):
    
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model = Note
        fields = ['id', 'content', 'username', 'time', 'photo_url']

    def get_photo_url(self, note):
        request = self.context.get('request')
        photo_url = note.photo.url
        return request.build_absolute_uri(photo_url)
    
class FavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = ['id_card', 'user']

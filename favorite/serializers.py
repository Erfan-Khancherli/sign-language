from rest_framework import serializers

from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id' , 'user' , 'word']
        ordering = ['user']
        read_only_fields = ['user']
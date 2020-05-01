from rest_framework import serializers

from apis.learnviews.models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['title', 'price', 'availability']
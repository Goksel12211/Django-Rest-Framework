import re
from wsgiref.validate import validator
from rest_framework import serializers

from watchlist_app.models import WatchList,StreamPlatform




class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model=StreamPlatform
        fields= "__all__"
     


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model=WatchList
        fields= "__all__"
     
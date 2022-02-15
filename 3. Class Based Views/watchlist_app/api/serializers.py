from rest_framework import serializers

from watchlist_app.models import Movie


class MovieSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description= serializers.CharField()
    active = serializers.BooleanField()
    
    
    #if create doesnt implement then Post methods in apiviews doesnt work.
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    
    
    # IF VALIDATED DATA get attributes is exists then assign instance attributes, else dont make changes. 
    def update(self,instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.active=validated_data.get('active',instance.active)
        instance.description=validated_data.get('description',instance.description)
        instance.save()
        return instance

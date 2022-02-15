import re
from wsgiref.validate import validator
from rest_framework import serializers

from watchlist_app.models import Movie


def is_too_long(value):
        if len(value)>20:
            raise serializers.ValidationError('Name is too long.')
    

class MovieSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name=serializers.CharField(validators=[is_too_long])
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
    
    #validate function's data parameter is OBJECT.
    def validate(self, data):
        if data['name']==data['description']:
            raise serializers.ValidationError("Name and Description should be diffrent !")
        else :
            return data
        
    def validate_name(self, value):
        if(len(value)<2):
            raise serializers.ValidationError("Name is too short.")
        else:
            return value
import re
from wsgiref.validate import validator
from rest_framework import serializers

from watchlist_app.models import Movie, Director




#Model Serializer does everything for us.  Deleted create update functions.
class MovieSerializer(serializers.ModelSerializer):    
    class Meta:
        model=Movie
        fields= "__all__"
        read_only_fields=['id']
     
    def get_len_name(self,object):
        return len(object.name)

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
        
        
        
        
        
    
class DirectorSerializer(serializers.ModelSerializer):
    # makaleler = MakaleSerializer(many=True, read_only=True)
    
       makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='makale-detay',
    )   
       class Meta:
        model = Director
        fields ='__all__' 


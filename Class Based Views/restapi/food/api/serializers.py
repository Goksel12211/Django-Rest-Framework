from  rest_framework import serializers
from food.models import Food

    #Modelsde seçilmese bile arka planda bir id oluşturulur.Serializerda id için bir alan açmalıyız.
class FoodSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    isFresh=serializers.BooleanField()


    #** olmasının sebebi    validated data arka planda bir dict dir . **  Anahtar değer alanlarını eşleştir
    # ve kaydetmesini sağlar. 
    def create(self,validated_data):
        print(validated_data)
        return Food.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.isFresh=validated_data.get('isFresh',instance.isFresh)
        return instance

from cv2 import exp
from django.shortcuts import render
from .models import Food
from .api.serializers import FoodSerializer

#Manual olarak HTTP 200 , 400 gibi cevaplamamız için .
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
class FoodListAPIView(APIView):
    def get(self,request):
        foods=Food.objects.all()
        serializer= FoodSerializer(foods,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer=FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class FoodDetailAPIView(APIView):
    
    def get_object(self,id):
        food_instance=get_object_or_404(Food, id=id)
        return food_instance

    def get(self,request,id):
        food_instance=self.get_object(id)
        serializer=FoodSerializer(food_instance)
        return Response(serializer.data)
    
    def put(self,request,id):
        food_instance=self.get_object(id=id) 
        serializer=FoodSerializer(food_instance,data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        food_instance=self.get_object(id=id)
        food_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        






@api_view(['GET','PUT','DELETE'])
def food_detail_api_view(request,food_id):
    try:
        food_instance=Food.objects.get(id=food_id)
    except Food.DoesNotExist:
        return Response(

            {'errors':{
                'code':404,
                'message':f"Boyle "+str(food_id)  +" ID li Food Yok."
            }}
            ,status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=FoodSerializer(food_instance)
        return Response(serializer.data)

    if  request.method=="PUT":
        serializer=FoodSerializer(food_instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATEDS)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method =="DELETE":
        food_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['GET','POST'])
def food_list_create_api_view(request):
    if request.method=='GET':
        foods=Food.objects.all()
        #Serializer tek bir nesne    üzerinden yazdık.Fakat foods fazladan elemanlı queryset
        serializer = FoodSerializer(foods,many=True)
        return Response(serializer.data)


        #ADAMLARDAN VERİ ALIRKEN
    if request.method=='POST':
        serializer = FoodSerializer(data=request.data)
        #Serializer modeldeki  alanları,alanlardaki şart ve limitleri bilir . Serializerdaki Gelen veri uygunsa is_valid true döner.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


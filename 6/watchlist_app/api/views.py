from urllib import response
from rest_framework.response import Response
from watchlist_app.models import WatchList,StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView




class StreamDetailAV(APIView):
    def get(self,request,id):
        try:
            movie=StreamPlatform.objects.get(id=id)
        except movie.DoesNotExist:
            return Response( {'error':'Movie not found.'} ,status=status.HTTP_404_NOT_FOUND )
        serializer=StreamPlatformSerializer(movie)
        return Response(serializer.data)
    
    
    def put(self,request,id):
        try:
            movie=StreamPlatform.objects.get(id=id)
        except movie.DoesNotExist:
            return Response( {'error':'Movie not found.'} ,status=status.HTTP_404_NOT_FOUND )
        
        serializer=StreamPlatformSerializer(movie,data=  request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error':'Bad Request.' }, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            movie=StreamPlatform.objects.get(id=id)
        except movie.DoesNotExist:
            return Response( {'error':'Movie not found.'} ,status=status.HTTP_404_NOT_FOUND )    
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

        
            
    




class StreamPlatformAV(APIView):
    def get(self,request):
        platform=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(platform,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchListAV(APIView):
    def get(self,request):
        movies=WatchList.objects.all()
        serializer=WatchListSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

        
class WatchDetailAV(APIView):
    def get(self,request,id):
        try:
            movie=WatchList.objects.get(id=id)
        except WatchList.DoesNotExist:
            return Response( {'error':'Movie not found.'} ,status=status.HTTP_404_NOT_FOUND )
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)
    
    
    def put(self,request,id):
        try:
            movie=WatchList.objects.get(id=id)
        except WatchList.DoesNotExist:
            return Response( {'error':'Movie not found.'} ,status=status.HTTP_404_NOT_FOUND )
        
        serializer=WatchListSerializer(movie,data=  request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error':'Bad Request.' }, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            movie=WatchList.objects.get(id=id)
        except WatchList.DoesNotExist:
            return Response( {'error':'Movie not found.'} ,status=status.HTTP_404_NOT_FOUND )    
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

        
            
    

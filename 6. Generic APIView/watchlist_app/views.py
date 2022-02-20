from django.http import JsonResponse
from django.shortcuts import render
from pydantic import Json
from watchlist_app.models import Movie
# Create your views here.

def movie_list(request):
    movies=Movie.objects.all()

    data={
        'movies':list(movies.values())
        }
    return JsonResponse(data)

def movie_detail(request,pk):
    movie=Movie.objects.get(id=pk)
    print(movie.name)
    data={
        'name'  : movie.name,
        'desc': movie.description,
        }
    return JsonResponse(data)

    
    

from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.views import View
from . import views

urlpatterns = [
    path('list/',views.movie_list,name="movie-list"),
    path('<int:pk>',views.movie_detail,name="movie-detail")
]

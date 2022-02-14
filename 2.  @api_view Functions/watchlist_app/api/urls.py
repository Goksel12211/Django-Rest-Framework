from django.urls import path,include
from watchlist_app.api.views import movie_list,movie_detail

urlpatterns = [
    path('list/',movie_list,name='movie_list'),
    path('<int:id>/',movie_detail,name='movie_detail')
]
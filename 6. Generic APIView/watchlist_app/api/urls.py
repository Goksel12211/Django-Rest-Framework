from django.urls import path,include
from watchlist_app.api.views import movie_list,movie_detail,MovieDetailAV,MovieListAV,DirectorListAV

urlpatterns = [
    path('list/',MovieListAV.as_view(),name='movie_list'),
    path('<int:id>/',MovieDetailAV.as_view(),name='makale-detay'),
    path('directors/',DirectorListAV.as_view(),name='director_list'),
]
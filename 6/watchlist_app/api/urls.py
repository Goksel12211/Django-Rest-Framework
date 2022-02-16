from unicodedata import name
from django.urls import path,include
from watchlist_app.api.views import WatchListAV,WatchDetailAV, StreamPlatformAV , StreamDetailAV

urlpatterns = [
    path('list/',WatchListAV.as_view(),name='movie_list'),
    path('<int:id>/',WatchDetailAV.as_view(),name='movie_detail'),
    path('stream/',StreamPlatformAV.as_view(),name='stream'),
    path('stream/<int:id>/',StreamDetailAV.as_view(),name="stream-detail")
]
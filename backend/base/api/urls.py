from django.urls import path,include
from . import views


from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

urlpatterns =[
    path('',views.getRoutes),
    
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    
]
"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import URLPattern, path,include
from food.views import food_list_create_api_view , food_detail_api_view, FoodDetailAPIView , FoodListAPIView

urlpatterns = [ 
    path('foods/',FoodListAPIView.as_view()),
    path('foods/<int:id>',FoodDetailAPIView.as_view())
]

#urlpatterns = [ 
#    path('foods/',food_list_create_api_view,name="food-list"),
#    path('foods/<int:food_id>',food_detail_api_view,name="food-get-by-id")
#]

from django.contrib import  admin


from django.urls import path,include
from books.api import views as api_view

urlpatterns=[
    path('books/',api_view.BookListCreateAPIView.as_view(),name='book_list')
]
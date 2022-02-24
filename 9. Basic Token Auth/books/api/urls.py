from django.contrib import  admin


from django.urls import path,include
from books.api import views as api_view

urlpatterns=[
    path('books/',api_view.BookListCreateAPIView.as_view(),name='book_list'),   
    path('books/<int:pk>',api_view.BookDetailAPIView.as_view(),name='book_detail'),
    path('books/<int:book_id>/create_comment',api_view.CreateCommentAPIView.as_view(),name='book_detail'),
]
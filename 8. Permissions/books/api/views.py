from django.shortcuts import get_object_or_404
from books.api.serializers import CommentSerializer,BookSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from books.models import Book,Comment
from rest_framework import generics,permissions

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [permissions.IsAdminUser]

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 

class CreateCommentAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def perform_create(self,serializer):
        book_id=self.kwargs['book_id']
        book=get_object_or_404(Book,id=book_id)     
        serializer.save(book=book)

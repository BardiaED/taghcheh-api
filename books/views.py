from rest_framework.generics import ListAPIView, RetrieveAPIView
from books.models import Book, AudioBook
from books.serializers import BookSerializer
from django.shortcuts import render

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def book_list_html(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/book_list.html', context)    

def audiobook_list_html(request):
    audiobooks = AudioBook.objects.all()
    context = {
        'audiobooks': audiobooks
    }
    return render(request, 'books/audiobook_list.html', context)
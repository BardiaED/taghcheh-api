from django.urls import path
from books.views import BookListAPIView, BookDetailAPIView, book_list_html, audiobook_list_html

urlpatterns = [
    path('all/', BookListAPIView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('html-list/', book_list_html, name='book-list-html'),
    path('html-audiobooks/', audiobook_list_html, name='audiobook-list-html'),
]
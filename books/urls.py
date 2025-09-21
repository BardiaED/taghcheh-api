from django.urls import path
from books.views import BookListAPIView, BookDetailAPIView

urlpatterns = [
    path('all/', BookListAPIView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
]
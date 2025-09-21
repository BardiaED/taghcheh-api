from django.contrib import admin
from .models import Author, Category, Book, Narrator, AudioBook

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Narrator)
admin.site.register(AudioBook)
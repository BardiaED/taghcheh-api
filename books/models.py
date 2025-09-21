from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title
    
class Narrator(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AudioBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    narrator = models.ForeignKey(Narrator, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    publication_date = models.DateField()
    duration_in_minutes = models.IntegerField()

    def __str__(self):
        return self.title    
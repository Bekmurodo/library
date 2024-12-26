from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    paper = models.CharField(max_length=50)

    def __str__(self):
        return self.title
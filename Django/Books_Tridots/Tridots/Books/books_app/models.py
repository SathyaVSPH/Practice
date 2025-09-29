from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField()
    author = models.CharField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.book_id} {self.title.title()} "
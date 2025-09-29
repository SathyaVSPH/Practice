from django.db import models

# Create your models here.
# I create a class Member

class Member(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    age = models.IntegerField(null = True)

    def __str__(self):
        return f'Name: {self.f_name} {self.l_name}\nAge: {self.age}'

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
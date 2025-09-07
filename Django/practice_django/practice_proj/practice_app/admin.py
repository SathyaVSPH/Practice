from django.contrib import admin
from .models import Member, Post

# Register your models here.

class Columns(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'age')

admin.site.register(Member, Columns)
admin.site.register(Post)

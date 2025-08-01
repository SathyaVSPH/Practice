from django.contrib import admin
from .models import Member

# Register your models here.

class Columns(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'age')

admin.site.register(Member, Columns)

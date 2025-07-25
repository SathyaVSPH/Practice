from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.greet, name='greet'),
    #path('', views.redirect_to_welcome, name='redirect'),
    path('', views.homepage, name='homepage'),
    path('project1', views.project1, name='Project1'),
    path('project2', views.members, name='Project2'),
]
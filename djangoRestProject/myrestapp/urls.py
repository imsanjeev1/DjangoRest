from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',home, name='home'),
    path('get-todo/',get_todo, name='get_todo'),
    path('post-todo/',post_todo, name='post_todo'),
    path('patch-todo/',patch_todo, name='patch_todo'),
    #class based view
    path('todo/',TodoView.as_view()),
    #End
]

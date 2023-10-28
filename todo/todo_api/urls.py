# from django.conf.urls import url
from django.urls import path, include

from .views import (
    TodoListAppView,
    TodoDetailApiView
)

urlpatterns = [
    path('api', TodoListAppView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
    
]
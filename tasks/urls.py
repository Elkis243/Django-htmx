from django.urls import path
from .views import *

app_name = "tasks" 

urlpatterns = [
    path('', Task.as_view(), name='post_task'),
    path('get_tasks/', get_tasks, name='get_tasks'),
]
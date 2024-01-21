from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('Update_task/<str:pk>', views.updateTask, name= "Update_task"),
    path('Delete_task/<str:pk>', views.deleteTask, name="Delete_task")
]
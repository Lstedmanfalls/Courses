from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #GET request to display all objects' info starting at root
    path('courses/create_course', views.create_course), #POST request to create an object
    path('courses/<int:course_id>', views.view_course), #GET request to display a specific object's info
    path('courses/<int:course_id>/destroy', views.delete_course), #POST request to delete a specific object
]
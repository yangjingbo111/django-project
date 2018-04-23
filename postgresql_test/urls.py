from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('next/', views.next, name='next'),
	path('add-city/', views.add_city, name='add_city'),
	path('delete-city/', views.delete_city, name='delete_city')
]
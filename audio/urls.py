from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('audio_stream/', views.audio_stream, name='audio_stream')
]
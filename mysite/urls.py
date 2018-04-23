"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from orderMenu import views

# Router provide an easy way of automatically determing the URL conf
router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/groups', views.GroupViewSet)
router.register(r'api/foods', views.FoodViewSet)

# wire up our API using automatic URL routing.
# Additionally, we include login URLS for the browserable API



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),    
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('hello/', include('myapp.urls')),
    path('food/', include('orderMenu.urls')),
    path('camera/', include('camera.urls')),
    path('map/', include('map.urls')),
    path('audio/', include('audio.urls')),
    path('postgresql_test/', include('postgresql_test.urls')),
]


from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Food

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'name')

class FoodSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Food
		fields = ('name', 'desc', 'price')
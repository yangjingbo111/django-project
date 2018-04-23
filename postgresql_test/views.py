from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Car, City
import requests

# Create your views here.
def index(request):
	queryset = City.objects.all()
	# context = {'data': queryset}
	cities = list(queryset)
	print(queryset)
	print(cities)

	all_weather = []
	for location in cities:
		weather_url = 'https://api.seniverse.com/v3/weather/now.json?key=s2220p2cscscragw&location={}&language=zh-Hans&unit=c'
		weather_json = requests.get(weather_url.format(location)).json()
		weather = {
			'location': weather_json['results'][0]['location']['name'],
			'text':		weather_json['results'][0]['now']['text'],
			'temp':		weather_json['results'][0]['now']['temperature'],
			'last_update': weather_json['results'][0]['last_update'][0:10] + ' '+ weather_json['results'][0]['last_update'][11:19] 
		}
		all_weather.append(weather)

	
	context = {'data': all_weather}
	# print(all_weather)
	# print(context)
	return render(request, 'postgresql_test/index.html', context)

def add_city(request):
	city = ''
	if request.method == 'GET':
		city = request.GET['city']
	
	# new_city = City.objects.create(name = city)
	# print(new_city)
	# print(city)
	# check repeat city
	has_city = list(City.objects.filter(name__iexact = city))
	# print(has_city.size)
	if len(has_city) == 0:
		new_city = City.objects.create(name = city)
		print('no city')	
	else:
		print('has city')

	return JsonResponse({})

def delete_city(request):
	city = ''
	if request.method == 'GET':
		city = request.GET['city']
	
	# check repeat city
	has_city = list(City.objects.filter(name__iexact = city).delete())
	# print(has_city.size)
	if len(has_city) == 0:
		print('delete failed')	
	else:
		print('delete ok')

	return JsonResponse({})

def next(request):
	print('next call')
	if request.method == 'GET':
		name = request.GET['name']
		print(name)
	
	queryset = Car.objects.all().values()
	context = {
		"data": list(queryset)
	}
	print(context)
	return JsonResponse(context)
	# return render(request, '', {'data': queryset})
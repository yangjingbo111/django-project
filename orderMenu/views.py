from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	# return HttpResponse("hello orderMenu")
	return render(request, 'orderMenu/index.html', {})
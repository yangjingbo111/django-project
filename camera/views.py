from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse,FileResponse
from django.views import View
from django.views.decorators import gzip
import cv2
import time

# Create your views here.
# class VideoCamera(View):
# 	def __init__(self):
# 		self.video = cv2.VideoCapture(0)

# 	def __del__(self):
# 		self.video.release()

# 	def get_frame(self):
# 		ret, image = self.video.read()
# 		ret,jpeg = cv2.imencode('.jpg', image)
# 		return jpeg.tobytes()

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield(b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + 
			frame + b'\r\n\r\n')

class VideoCamera():
	class __VideoCamera:
		def __init__(self):
			self.video = cv2.VideoCapture(0)

		def __del__(self):
			self.video.release()

		def get_frame(self):
			ret, image = self.video.read()
			ret, jpeg = cv2.imencode('.jpg', image)
			return jpeg.tobytes()

	instance = None
	def __new__(cls):
		if not VideoCamera.instance:
			VideoCamera.instance = VideoCamera.__VideoCamera()
		return VideoCamera.instance


# @gzip.gzip_page
# def index(request):
# 	try:
# 		response = StreamingHttpResponse(gen(VideoCamera()))
# 		response['Content-Type'] = "multipart/x-mixed-replace;boundary=frame"
# 		return response
# 	except HttpResponseServerError as e:
# 		print("aborted")

# def index(request):
# 	response = JsonResponse({'foo': 'bar'})
# 	return response

# def index(request):
# 	response = HttpResponse(gen(VideoCamera()))
# 	response['Content-Type'] = "multipart/x-mixed-replace;boundary=frame1"
# 	return response

# def index(request):
# 	response = HttpResponse()
# 	response['Content-Type'] = "multipart/related;boundary='frame1'"

# 	return response

def index(request):
	return render(request, "camera/index.html")

def stream(request):
	try:
		response = StreamingHttpResponse(gen(VideoCamera()))
		response['Content-Type'] = "multipart/x-mixed-replace;boundary=frame"
		return response
	except HttpResponseServerError as e:
		print("aborted")

# def index(request):
# 	response = FileResponse(open('E:\\images.jpg', 'rb'))	
# 	return response
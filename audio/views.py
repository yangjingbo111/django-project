from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse

import pyaudio

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024

# Create your views here.
def index(request):
	return render(request, 'audio/index.html', {})

def gen(audio):
	while True:
		frame = audio.get_frame()
		# print(frame)
		yield(frame)

class Audio():
	class __Audio:
		def __init__(self):
			self.audio = pyaudio.PyAudio()	
			self.stream = self.audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)

			print("recording...")		

		def __del__(self):
			self.stream.stop_stream()
			self.stream.close()
			self.audio.terminate()

		def get_frame(self):
			data = self.stream.read(CHUNK)
			return data

	instance = None
	def __new__(cls):
		if not Audio.instance:
			Audio.instance = Audio.__Audio()
		return Audio.instance


def audio_stream(request):
	try:
		response = StreamingHttpResponse(gen(Audio()),status=206)
		response['Content-Type'] = "audio/x-wav"
		return response
	except HttpResponseServerError as e:
		print("aborted")
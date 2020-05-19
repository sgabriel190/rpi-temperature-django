from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from .tasks import *

""", { 
            'temperature': info["temp"],
            'humidity': info["hum"],
            'local_time': info["time"],
         }
"""

class Index(View):
    path = "tempsens/index.html"

    def get(self, request):
        #info = getInfo()
        message = testTask.delay()
        return render(request, self.path, {'string': message.get() })


def disable_led(request):
    #powerOffLed()
    return redirect("")

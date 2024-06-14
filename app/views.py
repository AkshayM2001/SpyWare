from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Command


# Create your views here.
def home(request):
    return render(request, 'home.html')

def proxy_to_node(request):
    response = requests.get('http://127.0.0.1:3000/')
    return JsonResponse(response.json())

commands = ['list_app']

def fetch_commands(request):
    global commands
    if commands:
        command = commands.pop(0)
        return JsonResponse({'command': command})
    return JsonResponse({'command': None})

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Process received data (e.g., save to database)
        print("Received data:", data)
        return HttpResponse(status=200)
    return HttpResponse(status=400)

@csrf_exempt
def send_command(request):
    global commands
    if request.method == 'POST':
        command = request.POST.get('command')
        commands.append(command)
        return HttpResponse(status=200)
    return HttpResponse(status=400)

def command_form(request):
    return render(request, 'send_command.html')

def recieve(request):
    return render(request, 'recieve_data.html')

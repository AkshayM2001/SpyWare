from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Command


# Create your views here.
def home(request):
    return render(request, 'home.html')

def proxy_to_node(request):
    response = requests.get('http://127.0.0.1:3000/')
    return JsonResponse(response.json())


@csrf_exempt
def send_command(request):
    if request.method == 'POST':
        command_text = request.POST.get('command')
        Command.objects.create(command=command_text)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure', 'error': 'Invalid request'}, status=400)

@csrf_exempt
def fetch_commands(request):
    if request.method == 'GET':
        commands = Command.objects.all()
        command_list = [{'id': cmd.id, 'command': cmd.command} for cmd in commands]
        return JsonResponse({'status': 'success', 'commands': command_list})
    return JsonResponse({'status': 'failure', 'error': 'Invalid request'}, status=400)


def command_form(request):
    return render(request, 'send_command.html')

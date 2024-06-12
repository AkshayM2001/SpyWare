from django.shortcuts import render
import requests
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')

def proxy_to_node(request):
    response = requests.get('http://localhost:3000/')
    return JsonResponse(response.json())
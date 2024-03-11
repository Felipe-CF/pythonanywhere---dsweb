from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>DSWeb - 2024.1 - 20231014040005 - Felipe da Costa Ferreira</h1>")
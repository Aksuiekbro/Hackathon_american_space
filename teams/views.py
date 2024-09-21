from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Team

def index_search(request):
    return render(request, 'teams/Search/index.html')

def index(request):
    return HttpResponse("Hello, world. You're at the teams index.")

def teams(request):
    items = Team.objects.all()
    return render(request, "teams/Search/parse.html", {"Teams": items})
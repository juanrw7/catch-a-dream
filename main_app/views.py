from django.shortcuts import render
from .models import Dream


# Create your views here.

def home(request):
  return render(request, 'home.html')

def dream_index(request):
  dreams = Dream.objects.all()
  return render(request, 'dreams/index.html', {'dreams':dreams} )

def dream_detail(request, dream_id):
  dream = Dream.objects.get(id=dream_id)
  return render(request, 'dreams/detail.html', {'dream':dream})
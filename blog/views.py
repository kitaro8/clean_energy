from django.shortcuts import render, get_object_or_404
from .models import Post

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def hydropower(request):
    return render(request, 'blog/hydropower.html', {'title': 'Hydropower'})

def solar_power(request):
    return render(request, 'blog/solar_power.html', {'title': 'Solar Power'})


def wind_power(request):
    return render(request, 'blog/wind_power.html', {'title': 'Wind Power'})

def sources(request):
    return render(request, 'blog/sources.html', {'title': 'Sources'})

def home(request):
    return render(request, 'blog/home.html', {'title': 'Home'})


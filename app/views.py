from django.shortcuts import render
from app.models import Movie

def home(request):
    all = Movie.objects.all()
    context = {
        'movies': all,
    }
    return render(request, 'home.html', context)
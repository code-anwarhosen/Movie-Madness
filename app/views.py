from django.shortcuts import render
from app.models import Movie

def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'home.html', context)

def player(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'player.html', {'movie': movie})
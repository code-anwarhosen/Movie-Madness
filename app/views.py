from django.shortcuts import render
from app.models import Movie, Episode

def home(request):
    latest_uploaded = Movie.objects.filter(is_published=True).order_by('-timestamp')[:3]
    movies = Movie.objects.filter(is_series=False, is_published=True)
    series = Movie.objects.filter(is_series=True, is_published=True)
    upcoming = Movie.objects.filter(is_published=False)
    
    context = {
        'recently_added': latest_uploaded,
        'movies': movies,
        'upcoming': upcoming,
        'series': series,
    }
    return render(request, 'home.html', context)

def series(request, pk):
    web_s = Movie.objects.get(pk=pk)
    return render(request, 'series.html', {'series': web_s})

def player(request, pk):
    ref = request.GET.get('ref')

    if ref == 'series':
        movie = Episode.objects.filter(pk=pk).first()
    else:
        movie = Movie.objects.filter(pk=pk).first()
    return render(request, 'player.html', {'movie': movie})
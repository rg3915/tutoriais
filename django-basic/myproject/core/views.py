from django.shortcuts import render
# from django.http import HttpResponse
from .models import Movie


def home(request):
    return render(request, 'index.html')


def movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'core/movie_list.html', context)

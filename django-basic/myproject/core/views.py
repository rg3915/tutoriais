from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Movie


def home(request):
    return render(request, 'index.html')


def movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'core/movie_list.html', context)


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {'movie': movie}
    return render(request, 'core/movie_detail.html', context)

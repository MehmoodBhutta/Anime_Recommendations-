from django.shortcuts import render
from .models import Anime

def recommend_view(request):
    genre = request.GET.get('genre', '')
    recommendations = recommend_anime(genre) if genre else []
    return render(request, 'recommendations/recommend.html', {'recommendations': recommendations})

from django.shortcuts import render
from .models import Anime

def recommend_anime(genre):
    # This function will filter anime by genre
    return Anime.objects.filter(genre__icontains=genre).order_by('-rating')[:10]

def recommend_view(request):
    genre = request.GET.get('genre', '')
    recommendations = recommend_anime(genre) if genre else []
    return render(request, 'recommendations/recommend.html', {'recommendations': recommendations})

def recommend_view(request):
    genre = request.GET.get('genre', '')
    recommendations = recommend_anime(genre) if genre else []
    
    # Debug output
    print(f"Requested Genre: {genre}")
    print(f"Recommendations Count: {len(recommendations)}")

    return render(request, 'recommendations/recommend.html', {'recommendations': recommendations})

def recommend_view(request):
    genre = request.GET.get('genre', '')
    recommendations = recommend_anime(genre) if genre else []
    
    # Debug output
    print(f"Requested Genre: {genre}")
    print(f"Recommendations Count: {len(recommendations)}")

    return render(request, 'recommendations/recommend.html', {'recommendations': recommendations})

# views.py
from django.shortcuts import render
from .models import Anime

def anime_list(request):
    animes = Anime.objects.all()  # Fetch all anime data from the database
    return render(request, 'recommendations/anime_list.html', {'animes': animes})
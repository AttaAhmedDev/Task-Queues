from django.shortcuts import redirect, render

from .models import Movie
from .tasks import lookup_movie


def home(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            movie = Movie.objects.create(title=title)
            lookup_movie.delay(movie.id)
        return redirect("home")

    movies = Movie.objects.order_by("-created_at")
    return render(request, "movies/home.html", {"movies": movies})

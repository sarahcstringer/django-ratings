from django.shortcuts import render
from .models import Category, Movie, User, Rating
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Count

# Create your views here.


class MovieListview(generic.ListView):
    """General list of movies"""

    model = Movie


    def get_queryset(self):

        return Movie.objects.order_by('title')

    context['top_5'] = Movie.objects.annotate(ratings=Count('rating')).order_by('-ratings')[:5]

class MovieDetailView(generic.DetailView):
    """Detail page for a movie"""

    model = Movie
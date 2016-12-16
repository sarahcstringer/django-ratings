from django.shortcuts import render
from .models import Category, Movie, User, Rating
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.


class MovieListview(generic.ListView):
    """General list of movies"""

    model = Movie

    def get_queryset(self):

        return Movie.objects.order_by('title')


class MovieDetailView(generic.DetailView):
    """Detail page for a movie"""

    model = Movie
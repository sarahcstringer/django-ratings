from django.shortcuts import render
from .models import Category, Movie, User, Rating
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Count
from django.template import Context, Template

# Create your views here.

context = Context({})

class MovieListview(generic.TemplateView):
    """General list of movies"""

    model = Movie
    template_name = 'movies/movie_list.html'


    def get_context_data(self, **kwargs):

        context['top_5'] = Movie.objects.annotate(ratings=Count('rating')).order_by('-ratings')[:5]

        context['movie_list'] = Movie.objects.order_by('title')

        return context

class MovieDetailView(generic.DetailView):
    """Detail page for a movie"""

    model = Movie
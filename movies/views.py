from django.shortcuts import render
from .models import Category, Movie, User, Rating
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Count, Avg
from django.template import Context, Template


# Create your views here.

class MovieListview(generic.ListView):
    """General list of movies"""

    model = Movie
    template_name = 'movies/movie_list.html'

    # def get_context_data(self, **kwargs):
    #
    #     context = super(MovieListview, self).get_context_data(**kwargs)
    #
    #     context['5_most_rated'] = Movie.objects.annotate(ratings=Count('rating')).order_by('-ratings')[:5]
    #     context['5_highest_rated'] = Movie.objects.annotate(scores=Avg('rating__rating'),
    #                                                         cnt=Count('rating')).exclude(cnt__lt=5).order_by('-scores')[:5]
    #
    #     context['movie_list'] = Movie.objects.order_by('title')
    #
    #     return context

    paginate_by = 24


class MovieDetailView(generic.DetailView):
    """Detail page for a movie"""
    model = Movie

    # def get_queryset(self):
    #
    def get_context_data(self, **kwargs):
        obj = self.get_object()
        # print obj
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['num_ratings'] = obj.rating_set.count()
        return context


class RatingCreateView(generic.CreateView):
    """View for creating a rating"""
    model = Rating

    fields = ['user', 'movie', 'rating']

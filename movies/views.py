from .models import Category, Movie, User, Rating
from forms import MovieRatingForm
from django.urls import reverse
from django.utils.http import is_safe_url
from django.views import generic
from django.contrib import messages
from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login, 
    logout as auth_logout)
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
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


class MovieDetailView(generic.DetailView, generic.FormView):
    """Detail page for a movie"""
    model = Movie
    form_class = MovieRatingForm

    # def get_queryset(self):
    #
    def get_context_data(self, **kwargs):
        obj = self.get_object()
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['num_ratings'] = obj.rating_set.count()
        return context

    def get_initial(self):
        """Default selections"""

        return {
            'movie': self.get_object()
        }

    # def post(self):

class RatingCreateView(generic.CreateView):
    """View for creating a rating"""
    model = Rating

    fields = ['user', 'movie', 'rating']


class LoginView(generic.FormView):
    """Log in a user."""

    success_url = '/'
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    # def dispatch(self, request, *args, **kwargs):
    #     """Sets a test cookie to make sure the user has cookies enabled.
    #     """

    #     request.session.set_test_cookie()
    #     return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        return super(LoginView, self).form_valid(form)


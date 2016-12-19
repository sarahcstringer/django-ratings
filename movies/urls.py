from django.conf.urls import url

from .views import MovieListview, MovieDetailView, RatingCreateView

urlpatterns = [
    url(r'^$', MovieListview.as_view(), name='movies.movie_list'),
    url(r'^(?P<pk>[0-9]+)/$', MovieDetailView.as_view(), name='movies.movie_detail'),
    url(r'^create/$', RatingCreateView.as_view(), name='movies.rating_create'),
]
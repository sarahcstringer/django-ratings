from django.conf.urls import url

from .views import MovieListview, MovieDetailView

urlpatterns = [
    url(r'^$', MovieListview.as_view(), name='movies.movie_list'),
    url(r'^(?P<pk>[0-9]+)/$', MovieDetailView.as_view(), name='movies.movie_detail'),
]
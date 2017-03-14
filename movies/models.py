from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from django.utils.functional import cached_property

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name.title()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    released_at = models.DateField(blank=True)
    imdb_url = models.URLField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def get_categories_str(self):
        """Return the string of movie categories"""

        return ', '.join(category.category_name for category in self.category.all())

    def get_avg_rating(self):
        """Return the average rating for a movie"""

        sum_of_ratings = sum(rating.rating for rating in self.rating_set.all())
        return round(float(sum_of_ratings)/self.rating_set.count(), 2)

    def get_absolute_url(self):
        """URL for a movie detail view."""

        return reverse('movie_detail', kwargs={'pk': self.id})

    @cached_property
    def avg_rating(self):
        """Return movie's average rating"""
        sum_of_ratings = sum(rating.rating for rating in self.rating_set.all())
        return round(float(sum_of_ratings) / self.rating_set.count(), 2)


class User(models.Model):
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=5)
    age = models.PositiveSmallIntegerField()
    profession = models.CharField(max_length=50, default='other')
    gender = models.CharField(max_length=1, blank=True)

    def __str__(self):
        return 'Age: {}, G:{}, Z:{}, P:{}'.format(self.age, self.gender, self.zipcode, self.profession)

    def get_avg_usr_rating(self):
        """Return the average rating a user gives"""

        sum_of_ratings = sum(rating.rating for rating in self.rating_set.all())
        return round(float(sum_of_ratings)/self.rating_set.count(), 2)

    @cached_property
    def avg_rating(self):
        """Return the average user's rating"""
        sum_of_ratings = sum(rating.rating for rating in self.rating_set.all())
        return round(float(sum_of_ratings) / self.rating_set.count(), 2)


class Rating(models.Model):
    user = models.ForeignKey('User')
    movie = models.ForeignKey('Movie')
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'User: {}; Movie: {}; Score: {}'.format(self.user.id, self.movie.title, self.rating)
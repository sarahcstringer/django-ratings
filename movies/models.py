from __future__ import unicode_literals

from django.db import models

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


class User(models.Model):
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=5)
    age = models.PositiveSmallIntegerField()
    profession = models.CharField(max_length=50, default='other')
    gender = models.CharField(max_length=1, blank=True)

    def __str__(self):
        return 'Age: {}, G:{}, Z:{}, P:{}'.format(self.age, self.gender, self.zipcode, self.profession)


class Rating(models.Model):
    user = models.ForeignKey('User')
    movie = models.ForeignKey('Movie')
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'User: {}; Movie: {}; Score: {}'.format(self.user, self.movie, self.rating)





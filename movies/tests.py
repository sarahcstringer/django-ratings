from django.test import TestCase

from movies.models import Movie, Rating, User, Category

# Create your tests here.


class RatingTestCase(TestCase):
    def setUp(self):
        """Set up the test database"""

        self.m = Rating(user_id=1, movie_id=1, rating=5)

    def test_rating(self):
        """Can we create a rating instance?"""

        self.assertEqual(self.m.rating, 5)
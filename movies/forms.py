"""Forms for movie detail page"""

from django import forms
from django.db.models import IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator
# from django_select2.forms import Select2Widget
from models import Rating


class MovieRatingForm(forms.ModelForm):
    """Movie rating form"""

    # movie = forms.CharField(max_length=100)

    rating = IntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )

    class Meta:
        model = Rating
        fields = [
            'movie',
            # 'user',
            'rating',
        ]

from django.contrib import admin
from .models import Category, Movie, User, Rating

# Register your models here.
admin.site.register(Category)
# @admin.register(Category)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Admin view for movie"""

    list_display = ['id', 'title', 'released_at', 'get_categories_str', 'get_avg_rating']
    list_display_links = ['id', 'title']
    search_fields = ['title']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin view for user"""

    list_display = ['id', 'gender', 'zipcode', 'profession', 'get_avg_usr_rating']
    list_filter = ['profession']
    search_fields = ['email']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Admin view for rating"""

    list_display = ['movie', 'user', 'rating']
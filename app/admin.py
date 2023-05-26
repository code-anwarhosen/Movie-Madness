from django.contrib import admin
from app.models import Catagory, Movie, Series

admin.site.register(Catagory)
admin.site.register(Series)

class MovieAdmin(admin.ModelAdmin):
    raw_id_fields = ['series_name']
admin.site.register(Movie, MovieAdmin)
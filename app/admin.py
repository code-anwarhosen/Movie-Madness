from django.contrib import admin
from app.models import Catagory, Movie, Episode

admin.site.register(Catagory)
admin.site.register(Episode)

class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ['uid']
    ordering = ['-timestamp']
admin.site.register(Movie, MovieAdmin)
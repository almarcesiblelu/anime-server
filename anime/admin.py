from django.contrib import admin

# Register your models here.
from anime.models import Anime


class AnimeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Anime, AnimeAdmin)

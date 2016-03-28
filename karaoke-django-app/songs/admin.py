from django.contrib import admin

from .models import Performer, Song


# class PerformerInLine(admin.StackedInline):
#     model = Song


# class SongAdmin(admin.ModelAdmin):
#     inlines = [PerformerInLine,]

admin.site.register(Song)
admin.site.register(Performer)

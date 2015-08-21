from django.contrib import admin
from .models import *

# Register your models here.


class TextAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['headline', 'text', 'slug']})]
    prepopulated_fields = {'slug': ('headline',)}


class MediaAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'url', 'caption', 'credit', 'thumbnail', 'slug']})]
    prepopulated_fields = {'slug': ('title',)}


class TimelineAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'slug', 'text', 'media', 'published', 'options']})]
    prepopulated_fields = {'slug': ('title',)}


class EventAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'slug', 'start_date', 'end_date', 'timeline', 'media', 'text']})]
    list_display = ('title', 'start_date', 'end_date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'start_date', 'end_date']


admin.site.register(Timeline, TimelineAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Options)

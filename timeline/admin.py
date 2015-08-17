from django.contrib import admin
from .models import *

# Register your models here.


class MediaAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['headline', 'text', 'slug']})]
    prepopulated_fields = {'slug': ('headline',)}


class TimelineAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'slug', 'published']})]
    prepopulated_fields = {'slug': ('title',)}


class EventAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'slug', 'start_date', 'end_date', 'timeline', 'media', 'text']})]
    list_display = ('start_date', 'end_date')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Timeline, TimelineAdmin)
admin.site.register(Media)
admin.site.register(Text)
admin.site.register(Event, EventAdmin)



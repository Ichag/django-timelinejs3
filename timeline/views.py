import json

from django.views.generic.base import TemplateView
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404


from .models import Timeline, Options


def index_data(request, timeline_id):
    """Gets the last create timeline object and renders json for returning to template.
    timelinejs3 expects a json file, not able to read directly from json string"""
    if(timeline_id == 'latest'):
        obj = Timeline.objects.latest('id')
    else:
        obj = get_object_or_404(Timeline, pk=timeline_id)
    data = {
        "title": {
            "media": {
                "caption": obj.media and obj.media.caption or "",
                "credit": obj.media and obj.media.credit or "",
                "url": obj.media and str(obj.media.url) or "",
                "thumb": ""
            },
            "text": {
                "headline": obj.text and obj.text.headline or "",
                "text": obj.text and obj.text.text or ""
            }
        },
        "events": []
    }
    for event in obj.event_set.all():
        data['events'].append({
            "start_date": {
                "year": event and str(event.start_date.year) or "",
                "month": event and str(event.start_date.month) or "",
                "day": event and str(event.start_date.day) or "",
                "hour": event and str(event.start_date.hour) or "",
                "minute": event and str(event.start_date.minute) or "",
                "second": event and str(event.start_date.second) or "",
                "millisecond": "",
                "format": ""
            },
            "end_date": {
                "year": event and str(event.start_date.year) or "",
                "month": event and str(event.start_date.month) or "",
                "day": event and str(event.start_date.day) or "",
                "hour": event and str(event.start_date.hour) or "",
                "minute": event and str(event.start_date.minute) or "",
                "second": event and str(event.start_date.second) or "",
                "millisecond": "",
                "format": ""
            },
            "media": {
                "caption": event.media and str(event.media.caption) or "",
                "credit": event.media and str(event.media.credit) or "",
                "url": event.media and str(event.media.url) or "",
                "thumb": ""
            },
            "text": {
                "headline": event.text and event.text.headline or "",
                "text": event.text and event.text.text or ""
            },
        })

    return JsonResponse(data)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['timeline'] = Timeline.objects.all()
        context['options'] = Options.objects.latest('id')
        return context

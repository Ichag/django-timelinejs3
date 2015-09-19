from django.contrib import messages

from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from .models import *


def detail_data(request, timeline_id):
    """Gets the last create timeline object and renders json for returning to template.
    timelinejs3 expects a json file, not able to read directly from json string"""
    if timeline_id == 'latest':
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


class TimelineDetail(DetailView):

    model = Timeline


class IndexView(ListView):
    template_name = 'index.html'
    model = Timeline

    def get_queryset(self):
        return Timeline.objects.all()


class TimelineUpdate(UpdateView):

    model = Timeline
    fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('Saved'))
        return reverse('timeline_update_timeline', args=(self.object.pk,))


class TextUpdate(UpdateView):

    model = Text
    fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('Saved'))
        return reverse('timeline_update_text', args=(self.object.pk,))


class TimelineMediaDetail(DetailView):
    model = Media


class TimelineMediaUpdate(UpdateView):
    model = Media
    fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('Saved'))
        return reverse('timeline_update_media', args=(self.object.timeline.pk,))


class TimelineMediaCreateView(CreateView):
    model = Media
    fields = ('', '', )  # all without timeline

    def dispatch(self, request, *args, **kwargs):
        self.timeline = get_object_or_404(Timeline, pk=kwargs['pk'])
        return super(TimelineMediaCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.timeline = self.timeline
        return super(TimelineMediaCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('timeline_timeline_detail', args=(self.object.timeline.pk,))

    def get_context_data(self, **kwargs):
        kwargs['timeline'] = self.timeline
        return super(TimelineMediaCreateView, self).get_context_data(**kwargs)


class EventUpdate(UpdateView):

    model = Event
    fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('Saved'))
        return reverse('timeline_update_event', args=(self.object.pk,))


class OptionsPresetUpdate(UpdateView):

    model = OptionsPreset
    fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('Saved'))
        return reverse('timeline_update_optionspreset', args=(self.object.pk,))

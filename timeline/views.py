from django.contrib import messages
from django.forms import modelformset_factory

from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.shortcuts import get_object_or_404, render_to_response
from django.http import JsonResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _

from .models import *
from .forms import *


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
                "format": obj.time_format and str(obj.time_format) or "yyyy-dd-mm",
            },
            "end_date": {
                "year": event and str(event.end_date.year) or "",
                "month": event and str(event.end_date.month) or "",
                "day": event and str(event.end_date.day) or "",
                "hour": event and str(event.end_date.hour) or "",
                "minute": event and str(event.end_date.minute) or "",
                "second": event and str(event.end_date.second) or "",
                "millisecond": "",
                "format": obj.time_format and str(obj.time_format) or "yyyy-dd-mm",
            },
            "media": {
                "caption": event.media and str(event.media.caption) or "",
                "credit": event.media and str(event.media.credit) or "",
                "url": event.media and str(event.media.url) or "",
                "thumb": ""
            },
            "text": {
                "headline": event.text and event.text.headline or event.title,
                "text": event.text and event.text.text or ""
            },
        })

    return JsonResponse(data)


def event_date_format(argument):
    switcher = {
        0: ''
    }


class IndexView(ListView):
    template_name = 'index.html'
    model = Timeline

    def get_queryset(self):
        return Timeline.objects.all()


# Timeline Views
class TimelineDetail(DetailView):
    model = Timeline


class TimelineCreate(CreateView):
    model = Timeline
    fields = '__all__'


class TimelineUpdate(UpdateView):
    model = Timeline
    fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('Saved'))
        return reverse_lazy('index')


class TimelineDelete(DeleteView):
    model = Timeline
    success_url = reverse_lazy('index')


class TimelineMediaDetail(DetailView):
    model = Media


class TimelineMediaCreate(CreateView):
    model = Media
    fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('Saved'))
        return reverse('timeline_media_create')


class TimelineMediaDelete(DeleteView):
    model = Media

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('Saved'))
        return reverse_lazy('timeline_index')



class TimelineMediaUpdate(UpdateView):
    model = Media
    fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('Saved'))
        return reverse('timeline_media_detail', args=(self.object.timeline.media.pk,))


class TimelineTextDetail(DetailView):
    model = Text


class TimelineTextUpdate(UpdateView):
    model = Text
    fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('Saved'))
        return reverse('timeline_update_text', args=(self.object.timeline.text.pk,))


class TimelineTextCreate(CreateView):
    model = Text
    fields = '__all__'


class TimelineTextDelete(DeleteView):
    model = Text


class TimelineEventDetail(DetailView):
    model = Event


class TimelineEventUpdate(UpdateView):
    model = Event
    fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('Saved'))
        return reverse('timeline_update_event', args=(self.object.timeline.event_set.pk,))


class OptionsPresetUpdate(UpdateView):
    model = OptionsPreset
    fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('Saved'))
        return reverse('timeline_update_optionspreset', args=(self.object.pk,))


class TimelineCreateView(CreateView):
    model = Media
    fields = ('', '',)  # all without timeline

    def dispatch(self, request, *args, **kwargs):
        self.timeline = get_object_or_404(Timeline, pk=kwargs['pk'])
        return super(TimelineCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.timeline = self.timeline
        return super(TimelineCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('timeline_detail', args=(self.object.timeline.pk,))

    def get_context_data(self, **kwargs):
        kwargs['timeline'] = self.timeline
        return super(TimelineCreateView, self).get_context_data(**kwargs)

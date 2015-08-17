from django.db import models
from django.core import serializers

# important for translation
from django.utils.translation import ugettext_lazy as _


class Text(models.Model):
    headline = models.CharField(verbose_name=_('headline'), max_length=255)
    text = models.TextField(verbose_name=_('text'), blank=True)
    slug = models.SlugField(verbose_name=_('slug'), default="")

    def to_dict(self):
        return serializers.serialize("json", [self])

    def __str__(self):
        return self.slug


class Media(models.Model):
    url = models.URLField(verbose_name=_('url'), null=True, default="")
    caption = models.TextField(verbose_name=_('caption'), blank=True, null=True, default="")
    credit = models.TextField(verbose_name=_('credit'), blank=True, null=True, default="")
    thumbnail = models.URLField(verbose_name=_('thumbnail'), null=True, blank=True, default="")
    slug = models.SlugField(verbose_name=_('slug'), default="")

    def to_dict(self):
        return serializers.serialize("json", [self])

    def __str__(self):
        return self.slug


class BaseTimeline(models.Model):
    media = models.OneToOneField(to="timeline.Media", null=True, blank=True)
    text = models.OneToOneField(to="timeline.Text", null=True, blank=True)

    class Meta:
        abstract = True


class Event(BaseTimeline):
    title = models.CharField(verbose_name='internal Title', max_length=255, default="")
    start_date = models.DateTimeField(verbose_name=_('start_date'))
    end_date = models.DateTimeField(verbose_name=_('end_date'))
    timeline = models.ForeignKey(to='timeline.Timeline')
    slug = models.SlugField(verbose_name=_('slug'), default="")

    def to_dict(self):
        return serializers.serialize("json", [self])

    def __str__(self):
        return str(self.slug)


class Timeline(BaseTimeline):
    title = models.CharField(max_length=255)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(verbose_name=_('slug'), default="")

    def to_dict(self):
        return serializers.serialize("json", [self])

    def __str__(self):
        return self.title

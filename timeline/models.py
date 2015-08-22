from django.db import models
from django.core import serializers

# important for translation
from django.utils.translation import ugettext_lazy as _


class Text(models.Model):
    headline = models.CharField(verbose_name=_('headline'), max_length=255)
    text = models.TextField(verbose_name=_('text'), blank=True)
    slug = models.SlugField(verbose_name=_('slug'), default="")

    def __str__(self):
        return self.slug


class Media(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=255, default="")
    url = models.URLField(verbose_name=_('url'), null=True, default="")
    caption = models.TextField(verbose_name=_('caption'), blank=True, null=True, default="")
    credit = models.TextField(verbose_name=_('credit'), blank=True, null=True, default="")
    thumbnail = models.URLField(verbose_name=_('thumbnail'), null=True, blank=True, default="")
    slug = models.SlugField(verbose_name=_('slug'), default="")

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

    def __str__(self):
        return str(self.slug)


class OptionsPreset(models.Model):
    preset_title = models.CharField(max_length=255, default="")

    script_path = models.CharField(max_length=255, blank=True, default="")
    height = models.IntegerField(blank=True, default=0)
    width = models.IntegerField(blank=True, default=0)
    scale_factor = models.IntegerField(blank=True, null=True, default=3)
    layout = models.CharField(max_length=255, blank=True, default="landscape")

    TOP = "top"
    BOTTOM = "bottom"
    TIMENAV_POSTITION_CHOISES = (
        (TOP, 'Top'),
        (BOTTOM, 'Bottom')
    )
    timenav_position = models.CharField(max_length=6,
                                        choices=TIMENAV_POSTITION_CHOISES,
                                        default=BOTTOM, blank=True)
    optimal_tick_width = models.IntegerField(blank=True, null=True, default=100)
    base_class = models.CharField(max_length=255, blank=True, default="")
    timenav_height = models.IntegerField(blank=True, null=True, default=150)
    timenav_height_percentage = models.IntegerField(blank=True, null=True, default=25)
    timenav_height_min = models.IntegerField(blank=True, null=True, default=150)
    marker_height_min = models.IntegerField(blank=True, null=True, default=30)
    marker_width_min = models.IntegerField(blank=True, null=True, default=100)
    marker_padding = models.IntegerField(blank=True, null=True, default=5)
    start_at_slide = models.IntegerField(blank=True, null=True, default=0)
    menubar_height = models.IntegerField(blank=True, null=True, default=0)
    skinny_size = models.IntegerField(blank=True, null=True, default=650)
    relative_date = models.BooleanField(blank=True, default=False)
    use_bc = models.BooleanField(blank=True, default=False)
    duration = models.IntegerField(blank=True, null=True, default=1000)
    # ease:                       VCO.Ease.easeInOutQuint,
    dragging = models.BooleanField(blank=True, default=True)
    trackResize = models.BooleanField(blank=True, default=True)
    map_type = models.CharField(max_length=255, blank=True, default="stamen:toner-lite")
    slide_padding_lr = models.IntegerField(blank=True, null=True, default=100)
    slide_default_fade = models.IntegerField(blank=True, null=True, default=0)
    api_key_flickr = models.CharField(max_length=255, blank=True, default="")
    language = models.CharField(max_length=255, blank=True, default="en")

    def __str__(self):
        return self.preset_title


class Timeline(BaseTimeline):
    title = models.CharField(max_length=255)
    published = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(verbose_name=_('slug'), default="")

    options_preset = models.ForeignKey(to="timeline.OptionsPreset", verbose_name=_("the related option set"),
                                       blank=True, null=True)

    def __str__(self):
        return self.title

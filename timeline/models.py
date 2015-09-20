from django.core.urlresolvers import reverse
from django.db import models

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
    title = models.CharField(verbose_name='Title', max_length=255, default="")
    start_date = models.DateTimeField(verbose_name=_('start_date'))
    end_date = models.DateTimeField(verbose_name=_('end_date'))
    timeline = models.ForeignKey(to='timeline.Timeline')
    slug = models.SlugField(verbose_name=_('slug'), default="")

    def __str__(self):
        return str(self.slug)


class OptionsPreset(models.Model):
    preset_title = models.CharField(verbose_name=_("Preset Title"), max_length=255, default="")
    css_id = models.CharField(verbose_name=_("CSS ID for HTML Container"), max_length=255, default="timeline-embed")
    script_path = models.CharField(verbose_name=_("Path to TimelineJs Javascript File"), max_length=255, blank=True, default="")
    height = models.IntegerField(verbose_name=_("Container Height"), blank=True, default=0)
    width = models.IntegerField(verbose_name=_("Container Width"), blank=True, default=0)
    scale_factor = models.IntegerField(verbose_name=_("Scale factor"), help_text=_("How many screen widths wide should the timeline be"), blank=True, null=True, default=3)
    LANDSCAPE = "landscape"
    PORTRAIT = "portrait"
    LAYOUT_CHOISES = (
        (LANDSCAPE, 'Landscape'),
        (PORTRAIT, 'Portrait')
    )
    layout = models.CharField(verbose_name=_("Orientation"), max_length=9, choices=LAYOUT_CHOISES,
                              blank=True, default=LANDSCAPE)
    TOP = "top"
    BOTTOM = "bottom"
    TIMENAV_POSTITION_CHOISES = (
        (TOP, 'Top'),
        (BOTTOM, 'Bottom')
    )
    timenav_position = models.CharField(verbose_name=_("Position of the Navigation"), max_length=6,
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
    EASEINQUAD = "easeInQuad"
    EASEOUTQUAD = "easeOutQuad"
    EASEINOUTQUAD = "easeInOutQuad"
    EASEINCUBIC = "easeInCubic"
    EASEOUTCUBIC = "easeOutCubic"
    EASEINOUTCUBIC = "easeInOutCubic"
    EASEINQUART = "easeInQuart"
    EASEOUTQUART = "easeOutQuart"
    EASEINQUINT = "easeInQuint"
    EASEOUTQUINT = "easeOutQuint"
    EASEINOUTQUINT = "easeInOutQuint"
    EASE_CHOISES = (
        (EASEINQUAD, "easeInQuad"),
        (EASEOUTQUAD, "easeOutQuad"),
        (EASEINOUTQUAD, "easeInOutQuad"),
        (EASEINCUBIC, "easeInCubic"),
        (EASEOUTCUBIC, "easeOutCubic"),
        (EASEINOUTCUBIC, "easeInOutCubic"),
        (EASEINQUART, "easeInQuart"),
        (EASEOUTQUART, "easeOutQuart"),
        (EASEINQUINT, "easeInQuint"),
        (EASEOUTQUINT, "easeOutQuint"),
        (EASEINOUTQUINT, "easeInOutQuint"),
    )
    ease = models.CharField(max_length=255, choices=EASE_CHOISES, default=EASEINOUTQUINT)
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
    time_format = models.CharField(max_length=255, default="",
                                   help_text="Time format for events like yyyy-mm-dd - H:m:y")
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(verbose_name=_('slug'), default="")

    options_preset = models.ForeignKey(to="timeline.OptionsPreset", verbose_name=_("the related option set"),
                                       blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('timeline_detail',kwargs={'pk': self.pk})

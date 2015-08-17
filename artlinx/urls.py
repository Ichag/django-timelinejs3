from django.conf.urls import patterns, url
from timeline.views import IndexView

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name="index"),
)

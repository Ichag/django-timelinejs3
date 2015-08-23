from django.conf.urls import patterns, include, url
from django.contrib import admin
from timeline import views as timeline_views
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # name = app_(model)_action
    url(r'^timeline/$', timeline_views.IndexView.as_view(), name='timeline_index_latest'),
    url(r'^timeline/(?P<pk>[\d]+)/$', timeline_views.TimelineDetail.as_view(), name='timeline_detail'),
    url(r'^timeline/(?P<timeline_id>[\d]+)/data/$', timeline_views.detail_data, name='timeline_detail_data'),
    url(r'^timeline/(?P<pk>[\d]+)/update/text/$', timeline_views.TextUpdate.as_view(), name='timeline_update_text'),
    url(r'^timeline/(?P<pk>[\d]+)/update/timeline/$', timeline_views.TimelineUpdate.as_view(), name='timeline_update_timeline'),
    url(r'^timeline/(?P<pk>[\d]+)/update/event/$', timeline_views.EventUpdate.as_view(), name='timeline_update_event'),
    url(r'^timeline/(?P<pk>[\d]+)/update/options/$', timeline_views.OptionsPresetUpdate.as_view(), name='timeline_update_option'),
    url(r'^timeline/(?P<pk>[\d]+)/update/media/$', timeline_views.MediaUpdate.as_view(), name='timeline_update_media'),
]

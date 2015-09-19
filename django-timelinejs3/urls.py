from django.conf.urls import patterns, include, url
from django.contrib import admin
from timeline import views as timeline_views
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # name = app_(model)_action

    # set for timelinejs
    url(r'^timeline/$', timeline_views.IndexView.as_view(), name='timeline_index_latest'),
    url(r'^timeline/(?P<pk>[\d]+)/$', timeline_views.TimelineDetail.as_view(), name='timeline_detail'),
    url(r'^timeline/(?P<timeline_id>[\d]+)/data/$', timeline_views.detail_data, name='timeline_detail_data'),
    url(r'^timeline/text/(?P<pk>[\d]+)/update$', timeline_views.TextUpdate.as_view(), name='timeline_update_text'),
    url(r'^timeline/(?P<pk>[\d]+)/update/timeline/$', timeline_views.TimelineUpdate.as_view(), name='timeline_update_timeline'),
    url(r'^timeline/media/(?P<pk>[\d]+)/update/$', timeline_views.TimelineMediaUpdate.as_view(),
        name='timeline_media_update'),
]

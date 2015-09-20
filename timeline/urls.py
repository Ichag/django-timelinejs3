# All routes are defined in main project.
# Use your own routes to view methods
from django.conf.urls import url

from timeline import views as timeline_views

urlpatterns = [
    url(r'^$', timeline_views.IndexView.as_view(), name='timeline_index'),

    url(r'^(?P<timeline_id>[\d]+)/data/$', timeline_views.detail_data, name='timeline_detail_data'),

    # CRUD for Timeline
    url(r'^(?P<pk>[\d]+)/$', timeline_views.TimelineDetail.as_view(), name='timeline_detail'),
    url(r'^create/$', timeline_views.TimelineCreate.as_view(), name='timeline_create'),
    url(r'^(?P<pk>[0-9]+)/update/$', timeline_views.TimelineUpdate.as_view(), name='timeline_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', timeline_views.TimelineDelete.as_view(), name='timeline_delete'),

    # CRUD for media element
    url(r'^media/(?P<pk>[\d]+)/$', timeline_views.TimelineMediaDetail.as_view(), name='timeline_media_detail'),
    url(r'^media/create/$', timeline_views.TimelineMediaCreate.as_view(), name='timeline_media_create'),
    url(r'^media/(?P<pk>[\d]+)/update/$', timeline_views.TimelineMediaUpdate.as_view(), name='timeline_media_update'),
    url(r'^media/(?P<pk>[\d]+)/delete/$', timeline_views.TimelineMediaDelete.as_view(), name='timeline_media_delete'),

    # CRUD for text element
    url(r'^text/(?P<pk>[\d]+)/$', timeline_views.TimelineTextDetail.as_view(), name='timeline_text_detail'),
    url(r'^text/create/$', timeline_views.TimelineTextCreate.as_view(), name='timeline_text_create'),
    url(r'^text/(?P<pk>[\d]+)/update/$', timeline_views.TimelineTextUpdate.as_view(), name='timeline_text_update'),
    url(r'^text/(?P<pk>[\d]+)/delete/$', timeline_views.TimelineTextDelete.as_view(),name='timeline_text_delete'),

    # CRUD for event element
    url(r'^event/(?P<pk>[\d]+)/$', timeline_views.TimelineEventDetail.as_view(), name='timeline_event_detail'),
    url(r'^event/create/$', timeline_views.TimelineEventCreate.as_view(), name='timeline_event_create'),
    url(r'^event/(?P<pk>[\d]+)/update/$', timeline_views.TimelineEventUpdate.as_view(), name='timeline_event_update'),
    url(r'^event/(?P<pk>[\d]+)/delete/$', timeline_views.TimelineEventDelete.as_view(), name='timeline_event_delete'),

]

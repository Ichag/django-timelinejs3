from django.conf.urls import patterns, include, url
from django.contrib import admin
from timeline import views as timeline_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # name = app_(model)_action
    url(r'^timeline/latest$', timeline_views.IndexView.as_view(), name='timeline_index_latest'),
    url(r'^timeline/(?P<timeline_id>[\d]+)/$', timeline_views.IndexView.as_view(), name='timeline_detail'),

    url(r'^timeline/data/latest$', timeline_views.index_data, {'timeline_id': 'latest'}, name='timeline_index_data_latest'),
    url(r'^timeline/data/(?P<timeline_id>[\d]+)/$', timeline_views.index_data, name='timeline_index_data'),
]

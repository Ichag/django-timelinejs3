from django.conf.urls import patterns, include, url
from django.contrib import admin
from timeline import views as timeline_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # name = app_(model)_action
    url(r'^timeline/$', timeline_views.IndexView.as_view(), name='timeline_index'),
    url(r'^timeline/data/$', timeline_views.index_data, name='timeline_index_data'),
]
from django.conf.urls import include, url
from django.contrib import admin
from timeline import views as timeline_views
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # name = app_(model)_action

    # set for timelinejs
    url(r'^timeline/', include('timeline.urls')),
]

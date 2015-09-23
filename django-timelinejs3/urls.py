from django.conf.urls import include, url
from django.contrib import admin
from timeline import views as timeline_views
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.translation import ugettext_lazy
from registration.forms import UserRegistrationForm
from registration.views import RegistrationView

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^register/$', RegistrationView.as_view(), name='registration_register'),
    url(r'^admin/', include(admin.site.urls)),
    # set for timelinejs
    url(r'^timeline/', include('timeline.urls')),
]

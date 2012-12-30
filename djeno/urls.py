from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from tastypie.api import Api

from djeno.geno import views 
from djeno.geno import api

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(api.PersonResource())

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^', include('djeno.djeno_registration.backends.djeno.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

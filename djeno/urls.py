from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from djeno.geno import views

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

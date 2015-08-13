from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from requests import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)

urlpatterns = patterns('',
    url(r'^requests/', include('requests.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

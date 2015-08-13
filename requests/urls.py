from django.conf.urls import patterns, url

from requests import views

urlpatterns = patterns('',
	# ex: /requests/
    url(r'^$', views.index, name='index'),
    # ex: /requests/5/
    url(r'^(?P<request_id>\d+)/$', views.show, name='show'),
    # ex: /requests/5/edit/
    url(r'^(?P<request_id>\d+)/edit/$', views.edit, name='edit'),
    # ex: /requests/5/delete/
    url(r'^(?P<request_id>\d+)/delete/$', views.delete, name='delete'),
)

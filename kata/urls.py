from django.conf.urls.defaults import patterns, include, url

from myweb.kata.views import index, detail, edit, add, task_add, task_edit

urlpatterns = patterns('',
    url(r'^$', index),
		url(r'^detail/(\d+)$', detail),
		url(r'^edit/(\d+)', edit),
		url(r'^add/$', add),
		url(r'^task/$', task_add),
		url(r'^task/edit/(\d+)', task_edit),
)


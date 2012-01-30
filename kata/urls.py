from django.conf.urls.defaults import patterns, include, url

from kata.views import index, detail_project, edit_project, add_project, list_project, add_task, edit_task

urlpatterns = patterns('',
    url(r'detail/(\d+)$', detail_project, name='project_detail'),
    url(r'edit/(\d+)', edit_project, name='project_edit'),
    url(r'add/$', add_project, name='project_new'),
    url(r'task/(\d+)$', add_task, name='task_new'),
    url(r'task/edit/(\d+)', edit_task, name='task_edit'),
    url(r'list/$', list_project, name='project_list'),
    url(r'$', index, name='project_home'),
)


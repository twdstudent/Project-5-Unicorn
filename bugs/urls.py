from django.conf.urls import url, include
from .views import get_bugs, bugs_detail, create_or_edit_bug, upvote_bug, view_bug_detail 

urlpatterns = [
    url(r'^$', get_bugs, name='get_bugs'),
    url(r'^(?P<pk>\d+)/$', bugs_detail, name='bugs_detail'),
    url(r'^(?P<pk>\d+)/upvote/$', upvote_bug, name='upvote_bug'),
    url(r'^new/$', create_or_edit_bug, name='new_bug'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_bug, name='edit_bug'),
    url(r'^(?P<pk>\d+)/detail/$', view_bug_detail, name='bug_detail')
]

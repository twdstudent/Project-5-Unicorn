from django.conf.urls import url, include
from .views import get_bugs, bugs_detail, create_or_edit_bug, upvote_bug 

urlpatterns = [
    url(r'^$', get_bugs, name='get_bugs'),
    url(r'^upvote(?P<pk>\d+)/$', upvote_bug, name='upvote_bug'),
    url(r'^(?P<pk>\d+)/$', bugs_detail, name='bugs_detail'),
    url(r'^new/$', create_or_edit_bug, name='new_bug'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_bug, name='edit_bug')
]


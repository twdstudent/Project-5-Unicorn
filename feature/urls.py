from django.conf.urls import url, include
from .views import all_feature

urlpatterns = [
    url(r'^$', all_feature, name='feature'),
]
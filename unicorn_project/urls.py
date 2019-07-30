"""unicorn_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from accounts.views import index
from accounts import urls as accounts_urls
from bugs import urls as urls_bugs
from feature import urls as urls_feature
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from bugs.views import get_bugs, bugs_detail, create_or_edit_bug 
from feature.views import get_feature, feature_detail, create_or_edit_feature
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^$', RedirectView.as_view(url='bugs/')),
    url(r'^bugs/', include('bugs.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^$', RedirectView.as_view(url='feature/')),
    url(r'^feature/', include('feature.urls')),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
]


    
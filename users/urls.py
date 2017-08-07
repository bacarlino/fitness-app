from django.conf.urls import include, url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url('', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^test1/$', views.TestView.as_view(), name='test1'),
    url(r'^test2/$', views.test_view, name='test2')
]

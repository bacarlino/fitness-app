from django.conf.urls import url
from django.http import HttpResponse
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='tracker/base.html'), name='home')
]

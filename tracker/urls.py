from django.conf.urls import url
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='tracker/tracker_home.html'), name='home'),

    # url(r'^track/$', TemplateView.as_view(template_name='tracker/track_workout.html'), name='track'),

    url(r'^weight/$', views.track_weight, name='weight'),

    url(r'^workouts/$', views.WorkoutListView.as_view(), name='workouts'),

    url(r'^workout/(?P<pk>[\d+]+)/$', views.WorkoutDetailView.as_view(), name='workout-detail'),

    url(r'^track/$', views.WorkoutCreate.as_view(), name='track')
]

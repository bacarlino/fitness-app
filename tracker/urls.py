from django.conf.urls import url
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='tracker/tracker_home.html'), name='home'),

    # url(r'^track/$', TemplateView.as_view(template_name='tracker/track_workout.html'), name='track'),

    url(r'^weight/$', views.track_weight, name='weight'),

    url(r'^delete/(?P<id>\d+)/$', views.delete_weight, name='delete_weight'),

    url(r'^workouts/$', views.WorkoutListView.as_view(), name='workouts'),

    url(r'^workout/(?P<pk>[\d+]+)/$', views.WorkoutDetailView.as_view(), name='workout-detail'),

    url(r'^exercises/$', views.ExerciseListView.as_view(), name='exercises'),

    url(r'^exercise/(?P<pk>[\d+]+)/$', views.ExerciseDetailView.as_view(), name='exercise-detail'),

    url(r'^track/$', views.WorkoutCreate.as_view(), name='track'),

    url(r'^create-exercise/$', views.ExerciseCreate.as_view(), name='create-exercise')
]

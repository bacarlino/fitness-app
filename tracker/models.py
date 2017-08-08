from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Workout(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workout-detail', args=[str(self.id)])


class Sets(models.Model):
    weight = models.IntegerField(default=None, null=True)
    reps = models.IntegerField()
    workout = models.ForeignKey('Workout', default=None, null=True)
    exercise = models.ForeignKey('Exercise', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{0} - {1} lbs - {2} reps'.format(self.exercise, self.weight, self.reps)


class Exercise(models.Model):
    name = models.CharField(max_length=200, help_text='Exercise')
    muscle = models.ManyToManyField('Muscle', help_text='Muscle')

    def __str__(self):
        return self.name


class Muscle(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a muscle name')

    def __str__(self):
        return self.name

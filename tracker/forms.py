from django import forms
from .models import Workout, Weight, Exercise

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name']


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'muscle']


class LogWeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = ['weight']

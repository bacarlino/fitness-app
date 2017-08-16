from django import forms
from .models import Workout, Weight

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name']


class LogWeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = ['weight']

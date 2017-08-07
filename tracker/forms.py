from django import forms
from .models import Workout
from tracker.models import Weight

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name']


class LogWeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = ['weight']

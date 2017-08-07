from django.shortcuts import get_object_or_404, render
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Workout, Sets, Weight
from .forms import WorkoutForm, LogWeightForm
from django.urls import reverse
import datetime

def track_weight(request):
    if request.method == 'POST':
        form = LogWeightForm(request.POST)
        if form.is_valid():
            new_weight = Weight(
                weight=form.cleaned_data['weight'],
                user=request.user,
                created=datetime.datetime.now()
                )
            request.user.profile.current_weight = new_weight.weight
            new_weight.save()
            request.user.save()
            return redirect('weight', permanent=True)
    else:
        form = LogWeightForm()
    return render(request, 'tracker/weight.html', {'form': form})




class WorkoutListView(generic.ListView):
    model = Workout


class WorkoutDetailView(generic.DetailView):
    model = Workout


class WorkoutCreateView(CreateView):
    model = Workout
    fields = ['name']


class WorkoutCreate(generic.TemplateView):
    template_name = 'tracker/workout_create.html'

    def get(self, request, *args, **kwargs):
        workout_form = WorkoutForm()
        SetsFormSet = inlineformset_factory(Workout, Sets, fields=('weight', 'reps', 'exercise'), extra=1)
        formset = SetsFormSet()
        context = {'form': workout_form, 'formset': formset}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        workout_form = WorkoutForm(data=request.POST)
        SetsFormSet = inlineformset_factory(Workout, Sets, fields=('weight', 'reps', 'exercise'), extra=1)
        formset = SetsFormSet(data=request.POST)
        if workout_form.is_valid() and formset.is_valid():
            workout = workout_form.save()
            sets = formset.save(commit=False)
            for single_set in sets:
                single_set.workout = workout
                single_set.save()
            return HttpResponseRedirect('/')
        context = {'form': workout_form, 'formset': formset}
        return self.render_to_response(context)

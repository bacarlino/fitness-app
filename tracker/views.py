from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Workout, Sets, Weight, Exercise
from .forms import WorkoutForm, LogWeightForm, ExerciseForm
from django.urls import reverse
import calendar
import datetime
import pytz
from decimal import *

class FlowCalendar(calendar.HTMLCalendar):

    def formatmonth(self, year, month):
        pass





def view_calendar(request):
    pass



def track_weight(request):
    average_day = 0
    average_week = 0
    getcontext().prec = 5

    if request.method == 'POST':
        form = LogWeightForm(request.POST)
        if form.is_valid():
            new_weight = Weight(
                weight=form.cleaned_data['weight'],
                user=request.user
                )
            request.user.profile.current_weight = new_weight.weight
            new_weight.save()
            request.user.profile.save()
            return redirect('weight', permanent=True)

    else:
        weights = request.user.weight_set.order_by('created')
        weeks_weight_list = []
        todays_weight_list = []
        form = LogWeightForm()

        cal = calendar.HTMLCalendar().formatmonth(2018, 8)

        first_entry_date = weights[0].created
        print(weights)
        for weight in weights:
            print(weight.created)
        print('FIRST ENTRY DATE')
        print(first_entry_date)

        for weight in weights:
            if weight.created.date() == datetime.datetime.now(pytz.utc).date():
                todays_weight_list.append(weight.weight)
            if weight.created.weekday() == 0:
                break
            else:
                weeks_weight_list.append(weight.weight)

        if todays_weight_list:
            average_day = sum(todays_weight_list)/len(todays_weight_list)
        else:
            average_day = request.user.profile.current_weight

        if weeks_weight_list:
            getcontext().prec = 5
            average_week = sum(weeks_weight_list)/len(weeks_weight_list)
        else:
            average_week = request.user.profile.current_weight
    return render(request, 'tracker/weight.html', {'form': form, 'average_day': average_day, 'average_week': average_week, 'cal': cal})


def delete_weight(request, id):
    weight = get_object_or_404(Weight, pk=id)
    weight_set = request.user.weight_set.order_by('-created')
    if weight == weight_set[0] and len(weight_set) > 1:
        request.user.profile.current_weight = weight_set[1].weight
    request.user.profile.save()
    weight.delete()
    return HttpResponseRedirect(reverse('weight'))


class WorkoutListView(generic.ListView):
    model = Workout


class WorkoutDetailView(generic.DetailView):
    model = Workout


class WorkoutCreateView(CreateView):
    model = Workout
    fields = ['name']


class ExerciseListView(generic.ListView):
    model = Exercise


class ExerciseDetailView(generic.DetailView):
    model = Exercise


class ExerciseCreateView(CreateView):
    model = Exercise
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


class ExerciseCreate(generic.TemplateView):
    template_name = 'tracker/exercise_create.html'

    def get(self, request, *args, **kwargs):
        exercise_form = ExerciseForm()
        # SetsFormSet = inlineformset_factory(Workout, Sets, fields=('weight', 'reps', 'exercise'), extra=1)
        # formset = SetsFormSet()
        context = {'form': exercise_form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        exercise_form = ExerciseForm(data=request.POST)
        # SetsFormSet = inlineformset_factory(Workout, Sets, fields=('weight', 'reps', 'exercise'), extra=1)
        # formset = SetsFormSet(data=request.POST)
        if exercise_form.is_valid():
            exercise = exercise_form.save()
            # sets = formset.save(commit=False)
            # for single_set in sets:
            #     single_set.exercise = exercise
            #     single_set.save()
            return HttpResponseRedirect('/')
        context = {'form': exercise_form}
        return self.render_to_response(context)

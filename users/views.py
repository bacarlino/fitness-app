from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

from .forms import SignupForm, ProfileForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        p_form = ProfileForm(request.POST)
        if form.is_valid() and p_form.is_valid():
            user = form.save()
            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        p_form = ProfileForm()
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form, 'p_form': p_form})


@login_required(login_url='/users/login')
def profile(request):
    return render(request, 'users/profile.html')



class ProfileView(generic.DetailView):
    template_name = 'users/user_list.html'
    model = User


class TestView(generic.TemplateView):
    template_name = "test_template.html"
    whatever = "This is whatever I want it to be!"

    def get(self, request):
        return HttpResponse('<h1>' + self.whatever + '</h1>')

def test_view(request):

    context = {'whatever': 'This is whatever I want it to be!'}
    return render(request, 'test_template.html', context)

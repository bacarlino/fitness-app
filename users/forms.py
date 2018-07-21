from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #  Add the bootstrap class 'form-control' to each field
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
    })


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['current_weight', 'height_feet', 'height_inches', 'sex']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #  Add the bootstrap class 'form-control' to each field
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
    })

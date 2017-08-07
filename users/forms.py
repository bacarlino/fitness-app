from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #  Add the bootstrap class 'form-control' to each field
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
    })

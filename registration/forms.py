from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

JOBS = (
    ('backend', 'Backend'),
    ('frontend', 'Frontend'),
    ('mobile', 'Mobile')
)

class NewWorkerUserCreationForm(UserCreationForm):
    age = forms.IntegerField(required=True)
    city = forms.CharField(required=True)
    country = forms.CharField(required=True)
    nationality = forms.CharField(required=True)
    developer_type = forms.ChoiceField(choices=JOBS, required=True)
    main_language = forms.CharField(required=True)
    years_of_experience = forms.IntegerField(required=True)


    class Meta:
        model = models.NewWorkerUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'age',
            'city',
            'country',
            'nationality',
            'developer_type',
            'years_of_experience'
        )

        def save(self, commit=True):
            user = super(NewWorkerUserCreationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

class CustomAuthenticationForm(AuthenticationForm):
    pass
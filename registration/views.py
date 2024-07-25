from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import models, middlewares, forms
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(CreateView):
    form_class = forms.NewWorkerUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('registration:workerslogin')

    def form_valid(self, form):
        response = super().form_valid(form)
        years_of_experience = form.cleaned_data['years_of_experience']
        if years_of_experience >= 2 and years_of_experience <= 3:
            self.object.salary = 1000
        elif years_of_experience >= 4 and years_of_experience <= 5:
            self.object.salary = 2000
        elif years_of_experience > 5:
            self.object.salary = 3000
        else:
            self.object.salary = 0
        self.object.save()
        return response


class WorkRegisterView(LoginView):
    form_class = forms.CustomAuthenticationForm
    template_name = 'registration/login.html'


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('registration:workerslogin')


class WorkersListView(ListView):
    template_name = 'registration/workers_list.html'
    model = models.NewWorkerUser

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['salary'] = getattr(self.request, 'salary', 'Зарплата не определна')
        return context

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'
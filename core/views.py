from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from core.forms import UserForm


class TelaProtegida(TemplateView):
    template_name = 'protegida.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().get(request, args, kwargs)


class CustomLoginView(LoginView):
    template_name = 'auth.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, args, kwargs)


class NovoUsuario(CreateView):
    model = User
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    form_class = UserForm
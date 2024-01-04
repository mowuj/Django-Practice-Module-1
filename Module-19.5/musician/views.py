from django.shortcuts import render,redirect
from . import forms
from . models import Musician
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Type'] = 'Signup'
        return context

class UserLoginView(LoginView):
    template_name='register.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self,form):
        messages.success(self.request,'Logged in Successfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request, 'Logged in Information Invalid')
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['Type']='Login'
        return context

@method_decorator(login_required,name='dispatch')
class AddMusicianView(CreateView):
    model = Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')


@method_decorator(login_required, name='dispatch')
class EditMusicianView(UpdateView):
    model = Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class DeleteMusicianView(DeleteView):
    model = Musician
    pk_url_kwarg = 'id'
    template_name = 'delete.html'
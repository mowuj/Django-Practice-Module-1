from django.shortcuts import render,redirect
from .import forms
from . models import Album
# Create your views her
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):
    model=Album
    form_class=forms.AlbumForm
    template_name='add_album.html'
    success_url=reverse_lazy('add_album')


@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = Album
    form_class=forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = Album
    pk_url_kwarg='id'
    template_name='delete.html'

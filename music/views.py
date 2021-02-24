from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Album
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


class AlbumList(ListView):
    model = Album
    template_name = 'music/index.html'
    context_object_name = 'albums'


class AlbumDetail(DetailView):
    model = Album
    template_name = 'music/album-detail.html'
    context_object_name = 'album'


class AlbumCreate(CreateView):
    model = Album
    fields = ['album_title', 'artist', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['album_title', 'artist', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
                
        return render(request, self.template_name, {'form': form})

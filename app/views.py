from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.
class Top(ListView):
  model = Post
  
  
class Detail(DetailView):
  model = Post
  
class Create(CreateView):
  model = Post
  fields = ['project', 'description', 'category', 'team', 'pm', 'second_menber', 'third_menber', 'url']
  
  success_url = '/'
  
class Update(UpdateView):
  model = Post
  fields = ['project', 'description','category','team', 'pm', 'second_menber', 'third_menber', 'url']
  
  success_url = '/'
  
class Delete(DeleteView):
  model = Post
  
  success_url = '/'


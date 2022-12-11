from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from .models import Home 



class HomeListView(ListView): 
    template_name='home/home_list.html'
    model = Home 
    context_object_name = "AllHomes"

class HomeDetailView(DetailView): 
    template_name='home/home_detail.html'
    model = Home 

class HomeCreateView(CreateView): 
    template_name='home/home_create.html'
    model = Home 
    fields = ["owner","img_url","position", "description","rooms" ]

class HomeUpdateView(UpdateView):
    template_name='home/home_update.html'
    model = Home 
    fields = ["owner","img_url","position",  "description","rooms"] 

class HomeDeleteView(DeleteView):
    template_name='home/home_delete.html'
    model = Home
    success_url = reverse_lazy('home_list')

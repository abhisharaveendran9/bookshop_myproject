from django.shortcuts import render,redirect
from loginapp import forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView,CreateView,TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name: str="home.html"
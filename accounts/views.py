from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm



class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'

# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import MyUserCreationForm

# Create your views here.
class IndexView(View):

    def get(self, request):
        return render(request, 'home/index.html')


class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    model = User
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
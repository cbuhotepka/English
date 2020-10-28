from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('registration', views.RegistrationView.as_view(), name='registration'),  
    path('', views.IndexView.as_view(), name='index'),  
]
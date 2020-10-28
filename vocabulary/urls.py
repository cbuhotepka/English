from django.urls import path
from . import views

app_name = 'vocabulary'
urlpatterns = [
    path('word_list', views.WordListView.as_view(), name='word-list'),
    path('<str:word>', views.WordDetailView.as_view(), name='word-detail'),
]
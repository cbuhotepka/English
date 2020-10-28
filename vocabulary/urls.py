from django.urls import path
from . import views

app_name = 'vocabulary'
urlpatterns = [
    path('word_list', views.WordListView.as_view(), name='word-list'),
    path('search', views.SearchView.as_view(), name='search'),
    path('word/<str:word>', views.WordDetailView.as_view(), name='word-detail'),
]
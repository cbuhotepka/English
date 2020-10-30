from django.urls import path
from . import views

app_name = 'vocabulary'
urlpatterns = [
    path('word_list', views.WordListView.as_view(), name='word-list'),
    path('level/<str:lvl>', views.LevelView.as_view(), name='level'),
    path('search', views.SearchView.as_view(), name='search'),

    path('user_wordsets', views.UserWordsetListView.as_view(), name='user-wordset-list'),
    path('user_wordset/<int:pk>', views.UserWordsetDetailView.as_view(), name='user-wordset-detail'),
    path('user_wordset/<int:pk>/word_add', views.UserWordsetAddWord, name='wordset-add-word'),
    path('user_wordset/create', views.UserWordsetCreateView.as_view(), name='wordset-create'),
    path('user_wordset/<int:pk>/update', views.UserWordsetUpdateView.as_view(), name='wordset-update'),
    path('user_wordset/<int:pk>/delete', views.UserWordsetDeleteView.as_view(), name='wordset-delete'),

    path('word/<str:word>', views.WordDetailView.as_view(), name='word-detail'),
]
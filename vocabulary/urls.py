from django.urls import path
from . import views

app_name = 'vocabulary'
urlpatterns = [
    path('word_list', views.WordListView.as_view(), name='word-list'),
    path('level/<str:lvl>', views.LevelView.as_view(), name='level'),
    path('search', views.SearchView.as_view(), name='search'),

    path('vocabularies', views.UserVocabularyListView.as_view(), name='user-vocabulary-list'),
    path('user_vocabulary/<int:pk>', views.UserVocabularyDetailView.as_view(), name='user-vocabulary-detail'),

    path('word/<str:word>', views.WordDetailView.as_view(), name='word-detail'),
]
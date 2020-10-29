from django.urls import path
from . import views

app_name = 'vocabulary'
urlpatterns = [
    path('word_list', views.WordListView.as_view(), name='word-list'),
    path('level/<str:lvl>', views.LevelView.as_view(), name='level'),
    path('search', views.SearchView.as_view(), name='search'),

    path('user_vocabularies', views.UserVocabularyListView.as_view(), name='user-vocabulary-list'),
    path('user_vocabulary/<int:pk>', views.UserVocabularyDetailView.as_view(), name='user-vocabulary-detail'),
    path('user_vocabulary/<int:pk>/word_add', views.UserVocabularyAddWord, name='vocabulary-add-word'),
    path('user_vocabulary/create', views.UserVocabularyCreateView.as_view(), name='vocabulary-create'),
    path('user_vocabulary/<int:pk>/update', views.UserVocabularyUpdateView.as_view(), name='vocabulary-update'),
    path('user_vocabulary/<int:pk>/delete', views.UserVocabularyDeleteView.as_view(), name='vocabulary-delete'),

    path('word/<str:word>', views.WordDetailView.as_view(), name='word-detail'),
]
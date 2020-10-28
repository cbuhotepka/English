from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import View
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class WordDetailView(View):
    template_name = 'vocabulary/word_detail.html'

    def get(self, request, word):
        word_obj = get_object_or_404(Word, word=word)
        context = {'word':word_obj}
        return render(request, self.template_name, context)

class WordListView(View):
    template_name = 'vocabulary/word_list.html'

    def get(self, request):
        word_list = Word.objects.all().order_by('?')[:50].select_related('level')
        # word_list = Word.objects.filter(level__level='A1').order_by('?')[:50].select_related('level')

        context = {'word_list':word_list}
        return render(request, self.template_name, context)

class LevelView(View):
    template_name = 'vocabulary/level.html'

    def get(self, request, lvl):
        # word_list = Word.objects.all().order_by('?')[:50].select_related('level')
        word_list = Word.objects.filter(level__level=lvl).order_by('?')[:50].select_related('level')

        context = {'word_list':word_list, 'level':lvl}
        return render(request, self.template_name, context)

class SearchView(View):
    template_name = 'vocabulary/search.html'

    def get(self, request):
        search = request.GET['search']
        q = Q(word__icontains=search)
        q.add(Q(ru1__icontains=search), Q.OR)
        q.add(Q(ru2__icontains=search), Q.OR)
        search_list = Word.objects.filter(q)        
        context = {'search':search, 'search_list':search_list, 'number':len(search_list)}
        return render(request, self.template_name, context)

class UserVocabularyListView(LoginRequiredMixin, View):
    template_name = 'vocabulary/user_vocabulary_list.html'

    def get(self, request):
        vocabulary_list = UserVocabulary.objects.all()
        context = {'vocabulary_list':vocabulary_list}
        return render(request, self.template_name, context)

class UserVocabularyDetailView(LoginRequiredMixin, View):
    template_name = 'vocabulary/user_vocabulary_detail.html'

    def get(self, request, pk):
        vocabulary = get_object_or_404(UserVocabulary, pk=pk)
        word_vocabulary_list = WordVocabulary.objects.filter(vocabulary=vocabulary).select_related('word')
        context = {'vocabulary':vocabulary, 'word_vocabulary_list':word_vocabulary_list}
        return render(request, self.template_name, context)

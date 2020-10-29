from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from .models import *
from django.views.generic import View, CreateView, UpdateView, DeleteView
from .views_owner import OwnerCreateView, OwnerDeleteView, OwnerUpdateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserVocabularyForm
from .scripts.pictures import set_vocabulary_picture

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
        word_list = Word.objects.filter(q).select_related('level')
        context = {'search':search, 'word_list':word_list, 'number':len(word_list)}
        return render(request, self.template_name, context)

class UserVocabularyListView(LoginRequiredMixin, View):
    template_name = 'vocabulary/user_vocabulary_list.html'

    def get(self, request):
        vocabulary_list = UserVocabulary.objects.filter(user=request.user)
        context = {'vocabulary_list':vocabulary_list}
        return render(request, self.template_name, context)

class UserVocabularyDetailView(LoginRequiredMixin, View):
    template_name = 'vocabulary/user_vocabulary_detail.html'

    def get(self, request, pk):
        vocabulary = get_object_or_404(UserVocabulary, pk=pk, user=request.user)
        word_vocabulary_list = WordVocabulary.objects.filter(vocabulary=vocabulary).select_related('word')
        context = {'vocabulary':vocabulary, 'word_vocabulary_list':word_vocabulary_list}
        return render(request, self.template_name, context)

class UserVocabularyCreateView(OwnerCreateView):
    form_class = UserVocabularyForm
    success_url = reverse_lazy('vocabulary:user-vocabulary-list')
    template_name = 'vocabulary/user_vocabulary_create.html'

    def form_valid(self, form):
        vocabulary = form.save(commit=False)
        vocabulary.user = self.request.user
        vocabulary.save()
        set_vocabulary_picture(vocabulary)
        return super().form_valid(form)
        
class UserVocabularyUpdateView(OwnerUpdateView):
    form_class = UserVocabularyForm
    model = UserVocabulary
    success_url = reverse_lazy('vocabulary:user-vocabulary-list')
    template_name = 'vocabulary/user_vocabulary_update.html'

    # def get(self, request, pk, *args, **kwargs):
    #     self.object = get_object_or_404(UserVocabulary, pk=pk, user=self.request.user)
    #     return super().get(request, *args, **kwargs)

    # def post(self, request, pk):
    #     vocabulary = get_object_or_404(UserVocabulary, pk=pk, user=self.request.user)
    #     form = self.form_class(request.POST, instance=vocabulary)
    #     if not form.is_valid():
    #         context = {'form':form}
    #         return render(request, self.template_name, context)

    #     vocabulary = form.save(commit=False)
    #     vocabulary.save()
    #     return redirect(self.success_url)

class UserVocabularyDeleteView(OwnerDeleteView):
    model = UserVocabulary
    success_url = reverse_lazy('vocabulary:user-vocabulary-list')
    template_name = 'vocabulary/user_vocabulary_delete.html'

    # def post(self, request, *args, **kwargs):
    #     self.object = get_object_or_404(UserVocabulary, pk=kwargs['pk'], user=self.request.user)
    #     return self.delete(request, *args, **kwargs)

def UserVocabularyAddWord(request, pk):
    w_id = request.GET['w_id']
    v_id = pk
    word = get_object_or_404(Word, pk=w_id)
    vocabulary = get_object_or_404(UserVocabulary, pk=v_id, user=request.user)
    word_vocabulary, created = WordVocabulary.objects.get_or_create(vocabulary=vocabulary, word=word)
    try:
        success_url = request.META['HTTP_REFERER']
    except:
        success_url = reverse('vocabulary:user-vocabulary-detail')
    return redirect(success_url)
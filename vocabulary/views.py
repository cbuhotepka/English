from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from .models import *
from django.views.generic import View, CreateView, UpdateView, DeleteView
from .views_owner import OwnerCreateView, OwnerDeleteView, OwnerUpdateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserWordsetForm
from .scripts.pictures import set_wordset_picture
from .scripts.helpers import smart_split

# Create your views here.

# ==================== WORD VIEWS ====================

class WordDetailView(View):
    template_name = 'vocabulary/word_detail.html'

    def get(self, request, word):
        word_obj = get_object_or_404(Word, eng=word)
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
        q = Q(eng__icontains=search)
        q.add(Q(ru1__icontains=search), Q.OR)
        q.add(Q(ru2__icontains=search), Q.OR)
        word_list = Word.objects.filter(q).select_related('level')
        context = {'search':search, 'word_list':word_list, 'number':len(word_list)}
        return render(request, self.template_name, context)


# ==================== VOCABULARY VIEWS ====================

class UserWordsetListView(LoginRequiredMixin, View):
    template_name = 'vocabulary/user_wordset_list.html'

    def get(self, request):
        wordset_list = UserWordset.objects.filter(user=request.user).prefetch_related('words')
        context = {'wordset_list':wordset_list}
        return render(request, self.template_name, context)

class UserWordsetDetailView(LoginRequiredMixin, View):
    template_name = 'vocabulary/user_wordset_detail.html'

    def get(self, request, pk):
        wordset = get_object_or_404(UserWordset, pk=pk, user=request.user)
        word_wordset_list = WordWordset.objects.filter(wordset=wordset).select_related('word')
        context = {'wordset':wordset, 'word_wordset_list':word_wordset_list}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        wordset = get_object_or_404(UserWordset, pk=pk, user=self.request.user)

        if 'new_words' in request.POST:
            not_found = []
            for word in smart_split(request.POST['new_words']):
                print('=== HERE IS NEW WORD:', word)
                try:
                    word = Word.objects.get(eng=word)
                    word_wordset, created = WordWordset.objects.get_or_create(wordset=wordset, word=word)
                except Exception as ex:
                    print('--- EXCEPTION with:', word, ex)
                    not_found.append(word)
            print('--- NOT FOUND:', not_found)
            return redirect(request.path)

class UserWordsetCreateView(OwnerCreateView):
    form_class = UserWordsetForm
    success_url = reverse_lazy('vocabulary:user-wordset-list')
    template_name = 'vocabulary/user_wordset_create.html'

    def form_valid(self, form):
        wordset = form.save(commit=False)
        wordset.user = self.request.user
        wordset.save()
        set_wordset_picture(wordset)
        return super().form_valid(form)
        
class UserWordsetUpdateView(OwnerUpdateView):
    form_class = UserWordsetForm
    model = UserWordset
    success_url = reverse_lazy('vocabulary:user-wordset-list')
    template_name = 'vocabulary/user_wordset_update.html'

    # def get(self, request, pk, *args, **kwargs):
    #     self.object = get_object_or_404(UserWordset, pk=pk, user=self.request.user)
    #     return super().get(request, *args, **kwargs)

    def post(self, request, pk):
        wordset = get_object_or_404(UserWordset, pk=pk, user=self.request.user)

        if 'change_picture' in request.POST:
            set_wordset_picture(wordset)
            return redirect(self.request.path)

        form = self.form_class(request.POST, instance=wordset)
        if not form.is_valid():
            context = {'form':form}
            return render(request, self.template_name, context)

        wordset = form.save(commit=False)
        wordset.save()
        return redirect(self.success_url)

class UserWordsetDeleteView(OwnerDeleteView):
    model = UserWordset
    success_url = reverse_lazy('vocabulary:user-wordset-list')
    template_name = 'vocabulary/user_wordset_delete.html'

    # def post(self, request, *args, **kwargs):
    #     self.object = get_object_or_404(UserWordset, pk=kwargs['pk'], user=self.request.user)
    #     return self.delete(request, *args, **kwargs)

def UserWordsetAddWord(request, pk):
    w_id = request.GET['w_id']
    v_id = pk
    word = get_object_or_404(Word, pk=w_id)
    wordset = get_object_or_404(UserWordset, pk=v_id, user=request.user)
    word_wordset, created = WordWordset.objects.get_or_create(wordset=wordset, word=word)
    try:
        success_url = request.META['HTTP_REFERER']
    except:
        success_url = reverse('vocabulary:user-wordset-detail')
    return redirect(success_url)
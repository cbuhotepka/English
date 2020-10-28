from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import View
from django.db.models import Q

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

from vocabulary.models import WordWordset

def run():
    word_wordset_list = WordWordset.objects.all()
    for word_worset in word_wordset_list:
        print(word_wordset)
        word_worset.temporary = word_worset.vocabulary.id
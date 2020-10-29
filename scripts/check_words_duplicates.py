from vocabulary.models import Word

def run():
    word_list = Word.objects.all().order_by('word')
    for word in word_list:
        if Word.objects.filter(word=word.word).count() > 1:
            print(f"{word.word} - {word.ru1} / {word.ru2}")
            # word.delete()

    print('== DONE ==')
    
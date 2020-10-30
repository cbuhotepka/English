from vocabulary.models import Word

def run():
    word_list = Word.objects.all().order_by('eng')
    for word in word_list:
        if Word.objects.filter(eng=word.eng).count() > 1:
            print(f"{word.eng} - {word.ru1} / {word.ru2}")
            # word.delete()

    print('== DONE ==')
    
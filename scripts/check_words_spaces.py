from vocabulary.models import Word
ESCAPE = [
    'counter',
    'grave',
    'set',
]

def run():
    word_list = Word.objects.filter(eng__icontains=' ')
    for word in word_list:
        print(word.eng, '==>', word.eng.split()[0])
        if word.eng.split()[0] in ESCAPE:
            continue
        word.eng = word.eng.split()[0]
        word.save()
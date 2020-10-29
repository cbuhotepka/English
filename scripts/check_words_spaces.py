from vocabulary.models import Word
ESCAPE = [
    'counter',
    'grave',
    'set',
]

def run():
    word_list = Word.objects.filter(word__icontains=' ')
    for word in word_list:
        if word.word.split()[0] in ESCAPE:
            continue
        print(word.word, '==>', word.word.split()[0])
        word.word = word.word.split()[0]
        word.save()
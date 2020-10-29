from vocabulary.models import Word
ESCAPE = [
    'counter',
    'grave',
    'set',
]

def run():
    word_list = Word.objects.filter(word__icontains=' ')
    for word in word_list:
        print(word.word, '==>', word.word.split()[0])
        if word.word.split()[0] in ESCAPE:
            continue
        word.word = word.word.split()[0]
        word.save()
import csv
from vocabulary.models import Word, Level

# 0-word, 1-level, 2-ru1, 3-ru2

FILE = 'scripts\Oxford_3000-5000.csv'
def run():
    csv_handle = open(FILE)
    data = csv.reader(csv_handle, delimiter=';')
    i = 0
    print('\n>> START WITH: ', FILE)
    
    levels = {}
    for row in data:
        # print(row)
        if row[1] in levels:
            level = levels[row[1]]
        else:
            level, created = Level.objects.get_or_create(level=row[1])
            levels[row[1]] = level
        word, created = Word.objects.get_or_create(word=row[0])
        if created:
            word.level = level
            word.ru1 = row[2]
            if row[3] and row[3]!=' ':
                word.ru2 = row[3]
            word.save()
        #     print('>>Created WORD:', word)
        # else:
        #     print('--SKIPPED:', word)
        i+=1
        if i % 50 == 0:
            print(i)
            # break

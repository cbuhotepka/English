from vocabulary.models import Word
import requests
from time import sleep

def run():
    PATH = 'vocabulary\\static\\vocabulary\\audio\\'
    # SRC = 'https://howjsay.com/'
    SRC = 'https://d1qx7pbj0dvboc.cloudfront.net/'
    i=0
    for word in Word.objects.all():
        try:
            if not word.audio or word.audio==' ':
                url = SRC + word.word +'.mp3'
                r = requests.get(url)
                file_name = PATH + word.word +'.mp3'
                with open(file_name, 'wb') as f:
                    f.write(r.content)
                word.audio = word.word + '.mp3'
                word.save()
        except Exception as ex:
            print('--ERROR: ', ex, 'with', word.word)
        i+=1
        if i % 10 ==0:
            print(i)
            sleep(0.67)
        if i % 20 ==0:
            break
        sleep(0.3)
    

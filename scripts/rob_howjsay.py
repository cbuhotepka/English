from vocabulary.models import Word
import requests
from time import sleep

def run():
    PATH = 'vocabulary\\static\\vocabulary\\audio\\'
    # SRC = 'https://howjsay.com/'
    SRC = 'https://d1qx7pbj0dvboc.cloudfront.net/'
    i=0
    words = Word.objects.filter(audio='')
    count = len(words)
    for word in words:
        robbed = False
        try:
            # if not word.audio or word.audio==' ':
            url = SRC + word.eng +'.mp3'
            r = requests.get(url)
            file_name = PATH + word.eng +'.mp3'
            with open(file_name, 'wb') as f:
                f.write(r.content)
            word.audio = word.eng + '.mp3'
            word.save()
            robbed = True
        except Exception as ex:
            print(f"--ERROR: {ex} with {word.eng} {word.id}")
        i+=1
        if i % 20 ==0:
            print(f"{i} out of {count}")
            # sleep(0.67)
        if robbed:
            sleep(0.3)
    

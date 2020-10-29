# https://www.shutterstock.com/ru/search/phone?orientation=horizontal&image_type=photo

from vocabulary.models import Word
import requests
from time import sleep
import re
from random import choice

def run():
    HEADERS = {
        'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'cookie': 'yandexuid=9536276621592376392; yuidss=9536276621592376392; i=DgcyaBBAjSxHyvoYYsEgoDn7YRs2fLs7MSST+UlRvPfpUuj89UyhPlaTx39NAlZVKHml3Z7WcLqQZ4kZVyuJURKd7xo=; ymex=1907736392.yrts.1592376392#1907736392.yrtsi.1592376392; is_gdpr=0; is_gdpr_b=CIecPxCqCA==; yabs-sid=280899741603857787',
        'pragma': 'no-cache',
        # 'referer': 'https://www.shutterstock.com/ru/search/phone?orientation=horizontal&image_type=photo',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    }

    PATH = 'vocabulary\\static\\vocabulary\\image\\word\\'
    SRCH_HEAD = 'https://www.shutterstock.com/ru/search/'
    SRCH_TAIL = '?orientation=horizontal&image_type=photo'
    i=0
    word_list = Word.objects.filter(picture='')
    count = len(word_list)

    for word in word_list:
        robbed = False
        try:
            srch = word.word if ' ' not in word.word else word.word.split()[0]
            url = SRCH_HEAD + srch + SRCH_TAIL

            r = requests.get(url, headers=HEADERS)
            pics = re.findall(r"(https://image\.shutterstock\.com/.+?\.jpg)", r.content.decode())

            for j in range(3):
                pic_url = choice(pics)
                r_pic = requests.get(pic_url)
                if r_pic.status_code == 200:
                    break
            else:
                print(f"--NO PICTURE: {word.word}")
                continue

            # print(f"{word.word}: {pic_url}")

            file_name = word.word.replace(' ', '_').lower() +'.jpg'
            with open(PATH + file_name, 'wb') as f:
                f.write(r_pic.content)
            word.picture = file_name
            word.save()
            robbed = True

        except Exception as ex:
            print(f"--ERROR: {ex} with {word.word}")
        
        i+=1
        if i % 20 == 0:
            print(f"{i} out of {count}")
            # break
            # sleep(0.67)
        if robbed:
            sleep(0.3)
    

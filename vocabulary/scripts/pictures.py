# https://www.shutterstock.com/ru/search/phone?orientation=horizontal&image_type=photo

from vocabulary.models import UserWordset
import requests
from time import sleep
import re
from random import choice

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
PATH = 'vocabulary\\static\\vocabulary\\image\\wordset\\'
SRCH_HEAD = 'https://www.shutterstock.com/ru/search/'
SRCH_TAIL = '?orientation=horizontal&image_type=photo'

def set_wordset_picture(wordset):
    i=0
    try:
        url = SRCH_HEAD + wordset.title +SRCH_TAIL
        r = requests.get(url, headers=HEADERS)
        pics = re.findall(r"(https://image\.shutterstock\.com/.+?\.jpg)", r.content.decode())
        # print(r.content.decode()[:50])
        # pics = pics[:20]
        for i in range(20):
            pic_url = choice(pics)
            print(f"{wordset.title}: {pic_url}")
            r_pic = requests.get(pic_url)
            if r_pic.status_code == 200:
                break
        else:
            print(f"--NO PICTURE: {ex} with {wordset.title}")

        file_name = wordset.title.replace(' ', '_').lower() +'.jpg'
        with open(PATH + file_name, 'wb') as f:
            f.write(r_pic.content)
        wordset.picture = file_name
        wordset.save()
        robbed = True
    except Exception as ex:
        print(f"--ERROR: {ex} with {wordset.title}")
    

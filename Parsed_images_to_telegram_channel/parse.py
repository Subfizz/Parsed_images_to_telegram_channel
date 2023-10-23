from urllib.error import HTTPError, URLError

from ImageParser import YandexImage
import urllib.request
import random


def parse():
    f = open("dict.txt", encoding="utf-8")  # dictionary of your search requests
    dictionary = []
    lines = 0
    for i in f:
        lines += 1
        dictionary.append(f.readline())
    query = dictionary[random.randint(0, lines - 1)] + '4к'
    print(query)
    parser = YandexImage()
    search = query
    request = parser.search(search)
    if request:
        print('Connection is success')
    else:
        print('There is no connection')
    number = 0
    try:
        for item in request:
            number += random.randint(1, 3435435435)
            url = item.url
            size = item.size
            print(url)
            s = size.split("*")
            res = int(s[0]) * int(s[1])
            if res >= 2073600:
                if url.endswith('.jpg'):
                    img_url = 'C:/Users/user/Parsed_images_to_telegram_channel/images/picture' + str(number) + '.jpg'  # path of file
                    urllib.request.urlretrieve(url, img_url)
                elif url.endswith('.png'):
                    img_url = 'C:/Users/user/Parsed_images_to_telegram_channel/images/picture' + str(number) + '.png'
                    urllib.request.urlretrieve(url, img_url)
                elif url.endswith('.jpeg'):
                    img_url = 'C:/Users/user/Parsed_images_to_telegram_channel/images/picture' + str(number) + '.jpeg'
                    urllib.request.urlretrieve(url, img_url)
                elif url.endswith('.heic'):
                    img_url = 'C:/Users/user/Parsed_images_to_telegram_channel/images/picture' + str(number) + '.heic'
                    urllib.request.urlretrieve(url, img_url)
                else:
                    print('not supported')
            else:
                print('tiny resolution')

    except HTTPError as err:
        if err.code == 404:
            print(err.reason)
    except URLError as err:
        print("Some other error happened:", err.reason)

import random
import time
import os
import fnmatch
import requests


def upload():
    BOT_TOKEN = 'YOUR_API'  # Api
    CHANNEL_NAME = 'YOUR_CHAT_ID'  # chat_id
    listOfFiles = os.listdir('C:/Users/user/Parsed_images_to_telegram_channel/images/')  # path of dir
    pattern = "*.jpg"  # file type
    filenames = []
    count = 0
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            filenames.append(entry)
            count += 1

    def send_photo(BOT_TOKEN, CHANNEL_NAME):
        index = filenames[random.randint(0, count - 1)]
        img_url = 'C:/Users/user/Parsed_images_to_telegram_channel/images/' + index  # path of img
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        f = open(img_url, "rb")
        files = {"photo": f}
        data = {"chat_id": CHANNEL_NAME}
        response = requests.post(url, files=files, data=data)

        if response.status_code == 200:
            print("Photo send successful!")
            f.close()
            time.sleep(10)
            os.remove(img_url)
            filenames.remove(index)

        else:
            print("error when sending a photo.")

    send_photo(BOT_TOKEN, CHANNEL_NAME)

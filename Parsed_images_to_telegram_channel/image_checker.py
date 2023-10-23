import fnmatch

from PIL import Image, ImageChops
import os


def image_checker():
    listOfFiles = os.listdir('C:/Users/user/Parsed_images_to_telegram_channel/images/')  # directory of images
    pattern = "*.jpg"  # file type
    filenames = []
    count = 0
    temp_list = []
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            filenames.append(entry)
            count += 1
    print(filenames)
    for i in range(0, count):
        for j in range(i + 1, count):
            path1 = 'C:/Users/user/Parsed_images_to_telegram_channel/images/' + filenames[i]
            path2 = 'C:/Users/user/Parsed_images_to_telegram_channel/images/' + filenames[j]
            image_1 = Image.open(path1)
            image_2 = Image.open(path2)
            result = ImageChops.difference(image_1, image_2)
            diff = result.getbbox()
            if diff is None:
                temp_list.append(path1)
    for i in range(0, len(temp_list)):
        os.remove(temp_list[i])

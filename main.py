import schedule
import time

from image_checker import image_checker
from parse import parse
from upload import upload

schedule.every(39).minutes.do(parse)  # parse interval
schedule.every(46).minutes.do(image_checker)  # interval for checking for image duplicates
schedule.every(59).minutes.do(upload)  # photo upload interval
while True:
    schedule.run_pending()
    time.sleep(60)

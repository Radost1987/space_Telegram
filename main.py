import os
import time
from os import listdir
from pathlib import Path

import telegram
from dotenv import load_dotenv

from fetch_nasa import fetch_nasa_apod
from fetch_spacex import fetch_spacex_last_launch

while True:
    load_dotenv()
    bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))
    fetch_nasa_apod()
    fetch_spacex_last_launch()
    nasa_files = listdir('NASA images')
    for nasa_file in nasa_files:
        bot.send_document(chat_id=-1001586107729, document=open(
        f'{Path.cwd()}/NASA images/{nasa_file}', 'rb')
        )
        time.sleep(86400)
    spacex_files = listdir('SpaceX images')
    for spacex_file in spacex_files:
        bot.send_document(chat_id=-1001586107729, document=open(
        f'{Path.cwd()}/SpaceX images/{spacex_file}', 'rb')
        )
        time.sleep(86400)

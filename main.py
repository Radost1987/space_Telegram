import os
import time
from os import listdir
from pathlib import Path

import telegram
from dotenv import load_dotenv

from fetch_nasa import fetch_nasa_apod
from fetch_spacex import fetch_spacex_last_launch

def load_files_to_telegram(images_folder, path):
    load_dotenv()
    bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))
    files = listdir(images_folder)
    for file in files:
        with open(f'{path}/{file}', 'rb') as image:
            bot.send_document(
                chat_id=os.getenv('TELEGRAM_CHAT_ID'),
                document=image
            )
            time.sleep(86400)

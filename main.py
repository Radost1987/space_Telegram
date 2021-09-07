import os
import time
from pathlib import Path

import telegram
from dotenv import load_dotenv

from fetch_nasa import fetch_nasa_apod, fetch_nasa_epic
from fetch_spacex import fetch_spacex_last_launch
from folder_path_creater import create_folder_path


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


def main():
    while True:
        load_dotenv()
        telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
        telegram_token = os.getenv('TELEGRAM_TOKEN')
        nasa_api_key = os.getenv('NASA_API_KEY')
        nasa_image_folder = 'NASA images'
        spacex_image_folder = 'SpaceX images'
        create_folder_path(spacex_image_folder)


if __name__ == '__main__':
    main()

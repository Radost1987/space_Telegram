import os
import time
from os import listdir
from pathlib import Path

import telegram
from dotenv import load_dotenv

import fetch_nasa
import fetch_spacex

nasa_images_folder = 'NASA images'
spacex_images_folder = 'SpaceX images'


def create_images_path(images_folder):
    images_path = Path(f'{Path.cwd()}/{images_folder}')
    images_path.mkdir(parents=True, exist_ok=True)
    return images_path


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
        spacex_images_path = create_images_path(spacex_images_folder)
        nasa_images_path = create_images_path(nasa_images_folder)
        fetch_nasa.fetch_nasa_apod()
        fetch_nasa.fetch_nasa_epic()
        fetch_spacex.fetch_spacex_last_launch()
        load_files_to_telegram(nasa_images_folder, nasa_images_path)
        load_files_to_telegram(spacex_images_folder, spacex_images_path)


if __name__ == '__main__':
    main()

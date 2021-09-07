import os
import time
from pathlib import Path

import telegram
from dotenv import load_dotenv

from fetch_nasa import fetch_nasa_apod, fetch_nasa_epic
from fetch_spacex import fetch_spacex_last_launch
from folder_path_creater import create_folder_path


def load_files_to_telegram(image_folder, token, chat_id):
    bot = telegram.Bot(token=token)
    for path in Path(image_folder).iterdir():
        with open(f'{path}', 'rb') as image:
            bot.send_document(
                chat_id=chat_id,
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
        create_folder_path(nasa_image_folder)
        fetch_nasa_apod(nasa_api_key, nasa_image_folder)
        fetch_nasa_epic(nasa_api_key, nasa_image_folder)
        fetch_spacex_last_launch(spacex_image_folder)
        load_files_to_telegram(
            nasa_image_folder,
            telegram_token,
            telegram_chat_id
        )
        load_files_to_telegram(
            spacex_image_folder,
            telegram_token,
            telegram_chat_id
        )


if __name__ == '__main__':
    main()

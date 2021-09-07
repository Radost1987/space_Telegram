import datetime
import os

import requests
import urllib.parse
from dotenv import load_dotenv
from urllib.parse import urlsplit

from images_downloader import download_image
from folder_path_creater import create_folder_path


def get_extension(url):
    decoded_url = urllib.parse.unquote(url)
    path_url = urlsplit(decoded_url)
    extension = os.path.splitext(path_url.path)[1]
    return extension


def fetch_nasa_apod(nasa_api_key, nasa_image_folder):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_api_key,
        'count': 10
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images_info = response.json()
    for number, image in enumerate(images_info, start=1):
        extension = get_extension(image['url'])
        download_image(
            image['url'],
            nasa_image_folder,
            f'apod{number}{extension}'
        )


def fetch_nasa_epic(nasa_api_key, nasa_image_folder):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        'api_key': nasa_api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for number, image in enumerate(response.json(), start=1):
        created_date = datetime.datetime.fromisoformat(image['date']) \
            .strftime('%Y/%m/%d')
        download_image(
            f"https://epic.gsfc.nasa.gov/archive/natural/{created_date}/png/{image['image']}.png",
            nasa_image_folder,
            f'epic{number}.png'
        )


def main():
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')
    nasa_image_folder = 'NASA images'
    create_folder_path(nasa_image_folder)
    fetch_nasa_apod(nasa_api_key, nasa_image_folder)
    fetch_nasa_epic(nasa_api_key, nasa_image_folder)


if __name__ == "__main__":
    main()

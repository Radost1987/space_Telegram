import os

import requests
from pathlib import Path

import main
from images_downloader import download_images


def fetch_spacex_last_launch(image_folder):
    url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    for number, link in enumerate(links, start=1):
        download_image(link, image_folder, f'spacex{number}.jpg')

    spacex_image_folder = 'SpaceX images'
    create_folder_path(spacex_image_folder)
    fetch_spacex_last_launch(spacex_image_folder)


if __name__ == "__main__":
    main()

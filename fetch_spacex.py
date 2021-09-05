import os

import requests
from pathlib import Path

import main
from images_downloader import download_images


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    for i, link in enumerate(links, start=1):
        download_images(link, main.spacex_images_folder, f'spacex{i}.jpg')


if __name__ == "__main__":
    main.create_images_folders(main.spacex_images_folder)
    fetch_spacex_last_launch()

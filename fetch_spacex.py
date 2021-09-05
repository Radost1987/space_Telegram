import os

import requests
from pathlib import Path


def download_images(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(os.path.join('SpaceX images', filename), 'wb') as file:
        image = file.write(response.content)
    return image


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    for i, link in enumerate(links, start=1):
        download_images(link, f'spacex{i}.jpg')


if __name__ == "__main__":
    fetch_spacex_last_launch()

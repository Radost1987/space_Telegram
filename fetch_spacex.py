import requests

from images_downloader import download_image
from folder_path_creater import create_folder_path


def fetch_spacex_last_launch(image_folder):
    url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    for number, link in enumerate(links, start=1):
        download_image(link, image_folder, f'spacex{number}.jpg')


def main():
    spacex_image_folder = 'SpaceX images'
    create_folder_path(spacex_image_folder)
    fetch_spacex_last_launch(spacex_image_folder)


if __name__ == "__main__":
    main()

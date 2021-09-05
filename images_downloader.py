import os

import requests


def download_images(url, images_folder, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(os.path.join(images_folder, filename), 'wb') as file:
        image = file.write(response.content)
    return image

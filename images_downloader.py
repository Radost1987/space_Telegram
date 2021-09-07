import os

import requests


def download_image(url, image_folder, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(os.path.join(image_folder, filename), 'wb') as file:
        image = file.write(response.content)
    return image

from pathlib import Path


def create_folder_path(image_folder):
    folder_path = Path(f'{Path.cwd()}/{image_folder}')
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path

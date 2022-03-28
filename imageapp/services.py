import os.path
from io import BytesIO
from PIL import Image
import requests
from core.settings import MEDIA_ROOT

path = os.path.join(MEDIA_ROOT)


def resize_image(width, height, name):
    """Функция меняет разрешение изображения при помощи Pillow сохраняет """

    img = Image.open(f"{path}\\images\\{name}")
    img.resize((width, height))
    img.save(f"{path}\\images\\{width}_{height}_{name}")
    resize_path = f"{path}\\images\\{width}_{height}_{name}"

    return resize_path


def download_image(url):
    """Функция загружает изображения на локальный диск при помощи Pillow"""

    img = requests.get(url)
    io_bytes = BytesIO(img.content)
    image = Image.open(io_bytes, 'r')
    image.save(f"{path}\\images\\{img.url.split('/')[-1]}")
    image = Image.open(BytesIO(img.content))

    name = img.url.split('/')[-1]
    url = url
    picture = f"http://127.0.0.1:8000/media/images/{img.url.split('/')[-1]}"
    width = image.width
    height = image.height

    return name, url, picture, width, height


if __name__ == '__main__':
    download_image('https://www.notebookcheck-ru.com/fileadmin/_migrated/pics/eee_2_02.jpg')
    resize_image(500, 500, 'pexels-photo-11027273.jpeg')

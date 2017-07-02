from base64 import b64encode
import binqr
from tempfile import mkdtemp
import time
from uuid import uuid4
from os import path, listdir
from shutil import rmtree


def process(file):
    # Sleep para testar o famigerado ajax.gif (também conhecido como migué)
    time.sleep(1)

    images = binqr.convert(file)

    temp_dir = mkdtemp(prefix='binqr')

    for image in images:
        image.save(path.join(temp_dir, str(uuid4())))

    return temp_dir


def get_images(directory):
    encoded_images = []

    for file in listdir(directory):
        with open(path.join(directory, file), "rb") as image_file:
            encoded_string = b64encode(image_file.read()).decode()
            encoded_images.append(encoded_string)

    rmtree(directory)

    return encoded_images

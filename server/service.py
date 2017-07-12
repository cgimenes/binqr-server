from base64 import b64encode
import binqr
from tempfile import mkdtemp
from uuid import uuid4
from os import path, listdir
from shutil import rmtree


def process(filename, file):
    images = binqr.convert(filename, file)

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

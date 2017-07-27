import binqr
import imageio
from tempfile import mkdtemp
from uuid import uuid4
from os import path, listdir, remove
from shutil import rmtree
from base64 import b64encode


def process(filename, file):
    images = binqr.convert(filename, file)

    temp_dir = mkdtemp(prefix='binqr')

    for image in images:
        image.save(path.join(temp_dir, str(uuid4())))

    # Teste de GIF
    images = []
    for file in listdir(temp_dir):
        images.append(imageio.imread(path.join(temp_dir, file)))
        # remove(path.join(temp_dir, file))

    imageio.mimwrite(path.join(temp_dir, 'gif.gif'), images, fps=2)

    return temp_dir


def get_images(directory):
    encoded_images = []

    for file in listdir(directory):
        with open(path.join(directory, file), "rb") as image_file:
            encoded_string = b64encode(image_file.read()).decode()
            encoded_images.append(encoded_string)

    rmtree(directory)

    return encoded_images

import os

import shutil

from src.binqr import service


def test_process_9kb_file():
    filename = 'tests/binqr/9kb_file.png'

    with open(filename, 'rb') as file:
        byte_array = bytearray(file.read())

    tempdir = service.process(filename, byte_array)

    assert len(os.listdir(tempdir)) == 6

    shutil.rmtree(tempdir)


def test_getimages_9kb_file():
    filename = 'tests/binqr/9kb_file.png'

    with open(filename, 'rb') as file:
        byte_array = bytearray(file.read())

    tempdir = service.process(filename, byte_array)

    images = service.get_images(tempdir)

    assert len(images) == 6

    assert not os.path.exists(tempdir)

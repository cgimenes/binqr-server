from src.binqr import binqr


def test_static_convert():
    filename = 'tests/binqr/9kb_file.png'

    with open(filename, 'rb') as file:
        byte_array = bytearray(file.read())

    images = binqr.convert(filename, byte_array)

    assert len(images) == 5


def test_convert():
    filename = 'tests/binqr/9kb_file.png'

    with open(filename, 'rb') as file:
        byte_array = bytearray(file.read())

    images = binqr.BinQR().convert(filename, byte_array)

    assert len(images) == 5


def test_split_file():
    filename = 'tests/binqr/9kb_file.png'

    with open(filename, 'rb') as file:
        byte_array = bytearray(file.read())

    images_gen = binqr.BinQR().split_file(filename, byte_array)

    images = list(images_gen)

    assert len(images) == 5

    i = 1
    for image in images:
        assert image[0] == i
        assert image[1] == 5
        assert image[2] == 24
        i += 1


def test_calc_chunk_info():
    filename = 'tests/binqr/9kb_file.png'

    with open(filename, 'rb') as file:
        byte_array = bytearray(file.read())

    chunk_info = binqr.BinQR().calc_chunk_info(byte_array)

    assert chunk_info['size'] == 1816
    assert chunk_info['quantity'] == 5


def test_chunks():
    filename = 'tests/binqr/9kb_file.png'

    with open(filename, 'rb') as file:
        byte_array = bytearray(file.read())

    chunk_info = binqr.BinQR().calc_chunk_info(byte_array)

    chunks = binqr.BinQR().chunks(byte_array, chunk_info['size'])

    assert len(list(chunks)) == 5

def test_make_qr():
    filename = 'tests/binqr/9kb_file.png'

    with open(filename, 'rb') as file:
        byte_array = bytearray(file.read())

    images_gen = binqr.BinQR().split_file(filename, byte_array)

    images = list(images_gen)

    image = binqr.BinQR().make_qr(images[0])

    assert image.box_size == 2
    assert image.border == 4
    assert image.kind == "PNG"
    assert image.pixel_size == 330
    assert image.width == 157

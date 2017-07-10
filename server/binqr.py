import qrcode


def convert(file):
    images = []

    parts = _split_file(file)

    for part in parts:
        images.append(_make_qr(part))

    return images


def _make_qr(byte_list):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=2)

    qr.add_data(byte_list)
    qr.make(fit=True)

    return qr.make_image()


def _split_file(file):
    parts = []

    for i in range(0, _calc_parts_quantity_and_size(file)['quantity']):
        parts.append(file)

    return parts


def _calc_parts_quantity_and_size(file):
    return {'quantity': 5, 'part_size': len(file)}

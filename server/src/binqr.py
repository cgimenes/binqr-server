import qrcode


def convert(file):
    images = []

    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8
    )

    qr.add_data(file)
    qr.make(fit=True)

    images.append(qr.make_image())

    return images

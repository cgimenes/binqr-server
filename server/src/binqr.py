import qrcode


bytes_read = open("tes.png", "rb").read()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=8,
    border=4,
)

print(len(bytes_read))

qr.add_data(bytes_read)
qr.make(fit=True)

img = qr.make_image()
img.save('tes2.png')

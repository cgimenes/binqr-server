import hashlib
import qrcode


def convert(filename, file):
    return BinQR().convert(filename, file)


class BinQR:
    """
    Structure for each QR Code
    1 byte - compressed
    1 byte - number
    1 byte - quantity
    1 byte - filename length
    255 bytes - filename
    32 bytes - md5
    """

    MAX_QR_CODE_SIZE = 2500
    MAX_FILE_NAME_LENGTH = 255

    def convert(self, filename, file):
        parts = self.split_file(filename, file)

        images = []
        for part in parts:
            images.append(self.make_qr(part))

        return images

    def split_file(self, filename, file):
        chunk_info = self.calc_chunk_info(file)
        chunks = self.chunks(file, chunk_info['size'])
        filename_length = len(filename)
        filename_bytes = filename.encode('latin_1')
        checksum = hashlib.md5(file) # hashlib.md5(file).hexdigest()

        i = 1
        parts = []
        for chunk in chunks:
            parts.append(chunk)

        return parts

    def calc_chunk_info(self, file):
        file_length = len(file)
        divisor = 1
        chunk_size = file_length
        while True:
            if chunk_size <= self.MAX_QR_CODE_SIZE:
                break

            divisor += 1
            chunk_size = int(file_length / divisor)

        return {
            'size': chunk_size + 1,
            'quantity': divisor
        }

    @staticmethod
    def make_qr(byte_list):
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=2
        )

        qr.add_data(byte_list)
        qr.make(fit=True)

        return qr.make_image()

    @staticmethod
    def chunks(file, chunk_size):
        for i in range(0, len(file), chunk_size):
            yield file[i:i + chunk_size]

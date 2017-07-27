import qrcode


def convert(filename, file):
    return BinQR().convert(filename, file)


class BinQR:
    """
    QR Code metadata (258 bytes)
    1 byte - number
    1 byte - quantity
    1 byte - filename length
    255 bytes - filename
    """

    MAX_QR_CODE_SIZE = 2000
    MAX_FILE_NAME_LENGTH = 255

    def convert(self, filename, file):
        parts = self.split_file(filename, file)

        for part in parts:
            yield self.make_qr(part)

    def split_file(self, filename, file):
        chunk_info = self.calc_chunk_info(file)
        chunks = self.chunks(file, chunk_info['size'])
        chunks_quantity = chr(chunk_info['quantity']).encode('latin_1')
        filename_length = len(filename)
        hex_filename_length = chr(filename_length).encode('latin_1')
        filename_padding = (chr(0) * (self.MAX_FILE_NAME_LENGTH - filename_length)).encode('latin_1')
        filename_bytes = filename.encode('latin_1') + filename_padding

        i = 1
        for chunk in chunks:
            hex_number = chr(i).encode('latin_1')
            chunk_with_metadata = hex_number + chunks_quantity + hex_filename_length + filename_bytes + chunk

            yield chunk_with_metadata
            i += 1

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
            box_size=2,
            version=35
        )

        qr.add_data(byte_list, optimize=0)
        qr.make(fit=False)

        return qr.make_image()

    @staticmethod
    def chunks(file, chunk_size):
        for i in range(0, len(file), chunk_size):
            yield file[i:i + chunk_size]

import qrcode
import sys
from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from uuid import uuid4
from tempfile import mkdtemp
from os import listdir, path
from base64 import b64encode
from werkzeug.utils import secure_filename
import time

app = Flask(__name__)
app.secret_key = 'anachnu tov'


@app.route("/", methods=['GET'])
def index():
    if 'uid' not in session:
        session['uid'] = uuid4()
    return render_template('index.html')


@app.route("/success", methods=['GET'])
def success():
    if 'uid' not in session:
        return redirect(url_for('index'))

    encoded_images = []
    temp_dir = session['dir']

    for file in listdir(temp_dir):
        with open(path.join(temp_dir, file), "rb") as image_file:
            encoded_string = b64encode(image_file.read()).decode()
            encoded_images.append(encoded_string)

    session.clear()
    return render_template('success.html', images=encoded_images)


@app.route("/error", methods=['GET'])
def error():
    return render_template('error.html', vai=session['uid'])


@app.route("/process", methods=['POST'])
def process():
    # Sleep para testar o ajax
    time.sleep(3)

    if 'file' not in request.files:
        return jsonify(error='No file part'), 400

    file = request.files['file']

    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        return jsonify(error='No selected file'), 400

    bytes_read = file.read()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=4,
    )

    qr.add_data(bytes_read)
    qr.make(fit=True)

    img = qr.make_image()
    filename = secure_filename(file.filename)
    temp_dir = mkdtemp(prefix='binqr')
    img.save(path.join(temp_dir, filename))

    session['dir'] = temp_dir
    return '', 204


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

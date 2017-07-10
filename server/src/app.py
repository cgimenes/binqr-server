import service
from flask import Flask, render_template, session, redirect, url_for, request, jsonify


app = Flask(__name__)
app.secret_key = 'anachnu tov'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/success", methods=['GET'])
def success():
    if 'dir' not in session:
        return redirect(url_for('index'))

    encoded_images = service.get_images(session['dir'])

    session.clear()

    return render_template('success.html', images=encoded_images)


@app.route("/error", methods=['GET'])
def error():
    return render_template('error.html')


@app.route("/process", methods=['POST'])
def process():
    if 'file' not in request.files:
        return jsonify(error='No file part'), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify(error='No selected file'), 400

    bytes_read = file.read()
    session['dir'] = service.process(bytes_read)

    return '', 204


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

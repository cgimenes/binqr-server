from flask import Flask, render_template, session, redirect, url_for
from uuid import uuid4
app = Flask(__name__)
app.secret_key = 'anachnu tov'


@app.route("/", methods=['GET'])
def index():
    if 'uid' not in session:
        session['uid'] = uuid4()
    return render_template('index.html', vai=session['uid'])


@app.route("/success", methods=['GET'])
def success():
    return render_template('success.html', vai=session['uid'])


@app.route("/error", methods=['GET'])
def error():
    return render_template('error.html', vai=session['uid'])


@app.route("/process", methods=['POST'])
def process():
    return redirect(url_for('success'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    
# https://stackoverflow.com/questions/31542243/redirect-to-other-view-after-submitting-form
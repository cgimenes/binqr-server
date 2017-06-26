from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = 'anachnu tov'


@app.route("/", methods=['GET'])
def index():
    session['esse_eh_o_meu_parana'] = 'boa noite brasil'
    return render_template('index.html', vai='uso ou não uso a famigerada session?')


@app.route("/process", methods=['POST'])
def process():
    return

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = 'anachnu tov'


@app.route("/")
def index():
    session['esse_eh_o_meu_parana'] = 'boa noite brasil'
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
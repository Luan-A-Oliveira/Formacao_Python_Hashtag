from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Rebentando no flask em seloko</p>"

@app.route("/contatos")
def contato():
    return "<p>Manda um email ai!!</p>"


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


@app.route('/temp/')
def temp():
    return render_template("index.html")


@app.route('/name1/')
def name1():
    return "Hello, Marina"


@app.route('/<name>/')
def func_name(name):
    return f"<h1>Hello,</h1> {name}"


@app.route('/name/<names>/id/<number>/')
def func_names(names, number):
    number_user = int(number) * 100
    return f'<h1>Привет</h1>, <p><b>{names}</b> - <i>{number_user}</i></p>'


if __name__ == "__main__":
    app.run()

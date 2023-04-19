from flask import Flask, render_template, request
from pprint import pprint


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        print('processando requisição GET')

    if request.method == 'POST':
        print('processando requisição POST')

    pprint(vars(request))

    return render_template('form.html')


if __name__ == '__main__':
    app.run()

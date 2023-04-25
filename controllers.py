from flask import render_template, request
from pprint import pprint
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro')
def get_register():
    print('processando requisição GET')
    return render_template('form.html')


@app.route('/cadastro', methods=['POST'])
def post_register():
    print('processando requisição POST')
    pprint(request.form)
    return render_template('form.html')
from flask import render_template, request, session
from pprint import pprint
from app import app


@app.route('/')
def index():
    print('dados da sessão', vars(session))
    return render_template('index.html')


@app.route('/cadastro')
def register():
    print('processando requisição GET')
    return render_template('form.html')


@app.route('/confirmation', methods=['POST'])
def confirm():
    print('processando requisição POST')
    pprint(request.form)
    name = request.form.get('nome')
    telefone = request.form.get('tel')
    accept_whatsapp = request.form.get('accept-whatsapp')
    print('checkbox whatsapp', accept_whatsapp)

    dados = {
        'name': name,
        'telefone': telefone,
        'accept_whatsapp': accept_whatsapp
    }

    return render_template('confirmation.html', **dados)


@app.route('/login-get')
def login_get():
    print(request.args)
    usuario = request.args.get('user')
    senha = request.args.get('password')
    print('usuário', usuario)
    print('senha', senha)
    return render_template('login.html')


@app.route('/login-post', methods=['GET', 'POST'])
def login_post():
    print(request.method)
    if request.method.lower() == 'post':
        print('args', request.args)
        print('form', request.form)
        usuario = request.form.get('user')
        senha = request.form.get('password')
        print('usuário', usuario)
        print('senha', senha)
    return render_template('login-post.html')

from flask import render_template, request, session, redirect, url_for
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


@app.route('/login')
def login_get():
    return render_template('login.html')


usuario1 = {'login': 'rafael', 'senha': 'asdf1234'}


@app.route('/login', methods=['POST'])
def login_post():
    print('form', request.form)
    usuario = request.form.get('user')
    senha = request.form.get('password')

    # validação do usuário aqui
    if not usuario == usuario1['login']:
        return "usuário não encontrado"

    if not senha == usuario1['senha']:
        return "senha incorreta"

    return redirect(url_for('area_logada'))


@app.route('/area-logada')
def area_logada():
    return render_template('area-logada.html')

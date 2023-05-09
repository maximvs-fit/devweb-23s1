import uuid

from app import app
from flask import redirect, render_template, request, session, url_for, make_response


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

    dict_usuario = {'nome': usuario}

    id_sessao = str(uuid.uuid1())
    session.update({id_sessao: dict_usuario})

    print('sessão do servidor', session)
    resposta = make_response(redirect(url_for('area_logada')))
    resposta.set_cookie('session-id', id_sessao)
    resposta.set_cookie('teste', '123')

    return resposta


@app.route('/logout')
def logout():
    id_sessao = request.cookies.get('session-id')
    usuario = session.pop(id_sessao, None)

    if usuario is None:
        print('usuario já não existia!')
    resposta = make_response(redirect(url_for('login_get')))
    resposta.set_cookie('session-id', '')

    return resposta

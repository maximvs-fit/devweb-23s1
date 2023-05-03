from flask import render_template, request, session, redirect, url_for
from app import app


@app.route('/area-logada')
def area_logada():
    print('cookies', request.cookies)
    id_sessao = request.cookies.get('session-id')

    usuario = session.get(id_sessao)
    if usuario is None:
        print('não está logado')
        return redirect(url_for('login_get'))

    print('usuario', usuario)

    return render_template('area-logada.html')

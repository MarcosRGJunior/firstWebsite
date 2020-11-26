from datetime import datetime
from flask import render_template, request, redirect, flash, session
from . import website_bp
from funcoes import listar_partida, obter_equipe, obter_partida_equipe, obter_resultado, validar_user


@website_bp.route('/')
def home():
    lista_partida = listar_partida()
    return render_template('home.html', lista_partida=lista_partida)


@website_bp.route('/equipe/<sigla>')
def equipe(sigla):
    sigla_equipe = obter_equipe(sigla)
    partidas = obter_partida_equipe(sigla)
    resultados = obter_resultado(sigla)
    return render_template('equipe.html', equipe=sigla_equipe, partidas=partidas, resultados=resultados)


@website_bp.route('/entrar', methods=['GET', 'POST'])
def entrar():
    erros = []
    if request.method == 'POST':
        form = request.form
        login = form.get('login-email')
        senha = form.get('login-senha')

        validacao = validar_user(login, senha)
        if validacao == True:
            session['usuario'] = login
            print(session['usuario'])
            session['data'] = datetime.now()
            print(session['data'])
            return redirect('/admin')
        else:
            flash('Algo errado nas Credenciais')
            return render_template('admin/credenciais.html')
    else:
        return render_template('entrar.html')

@website_bp.route('/sair')
def sair():
    session.clear()
    return redirect('/')	
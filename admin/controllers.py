from flask import render_template, request, redirect, flash, session
from . import admin_bp
from funcoes import listar_partida, obter_equipe, obter_partida_equipe, obter_resultado, validar_user, excluir_equipe, incluir_equipe, alterar_equipe, incluir_partida, excluir_partida, alterar_partida
from dados import *


@admin_bp.route('/admin/')
def home_admin():
    if not 'usuario' in session:
       return redirect('/entrar')
    else:
        lista_partida = listar_partida()
        return render_template('admin/home.html', lista_partida=lista_partida)


@admin_bp.route('/admin/det_equipe/<sigla>')
def equipe_admin(sigla):
    if not 'usuario' in session:
       return redirect('/entrar')
    else:
        sigla_equipe = obter_equipe(sigla)
        partidas = obter_partida_equipe(sigla)
        resultados = obter_resultado(sigla)
        return render_template('admin/equipe.html', equipe=sigla_equipe, partidas=partidas, resultados=resultados)

@admin_bp.route('/admin/equipe/', methods=['GET', 'POST'])
def admin_equipe():
    if not 'usuario' in session:
       return redirect('/entrar')
    else:
        return render_template('admin/equipe.html', equipes=EQUIPES)


@admin_bp.route('/admin/excluir/<sigla>')
def excluir(sigla):
    if not 'usuario' in session:
       return redirect('/entrar')
    else:
        validacao = excluir_equipe(sigla)
        if validacao == True:
            return redirect('/admin/equipe')
        else:
            return redirect('/')


@admin_bp.route('/admin/equipe/criar', methods=['GET', 'POST'])
def criar():
    if not 'usuario' in session:
       return redirect('/entrar')
    else:
        erros = None
        if request.method == 'POST':
            form = request.form
            erros = incluir_equipe(
                form.get('equipe-nome'), form.get('equipe-sigla'), form.get('equipe-local'))
            if len(erros) == 0:
                return redirect('/admin/equipe/')

        return render_template('admin/equipe_form.html', equipes=EQUIPES, erros=erros, equipe=None)


@admin_bp.route('/admin/equipe/alterar/<sigla>', methods=['GET', 'POST'])
def alterar(sigla):
    if not 'usuario' in session:
       return redirect('/entrar')
    else:
        erros = None
        equipe = obter_equipe(sigla)
        if request.method == 'POST':
            form = request.form
            erros = alterar_equipe(
                form.get('equipe-nome'), sigla, form.get('equipe-sigla'), form.get('equipe-local'))
            if len(erros) == 0:
                return redirect('/admin/equipe/')

        return render_template('admin/equipe_form.html', equipes=EQUIPES, erros=erros, equipe=equipe)


@admin_bp.route('/admin/partida')
def admin_partida():
    if not 'usuario' in session:
       return redirect('/entrar')
    else:
        return render_template('admin/partida.html', partidas=PARTIDAS)


@admin_bp.route('/admin/partida/criar', methods=['GET', 'POST'])
def criar_partida():
    if not 'usuario' in session:
       return redirect('/entrar')
    else:
        erros = None
        if request.method == 'POST':
            form = request.form
            erros = incluir_partida(
                form.get('partida-equipe_casa'), form.get('partida-equipe_visita'), form.get('partida-pontos_casa'), form.get('partida-pontos_visita'))
            if len(erros) == 0:
                return redirect('/admin/partida')
        
        return render_template('admin/partida_form.html', equipes=EQUIPES, erros=erros, partidas=[1], index=0)

@admin_bp.route('/admin/partida/excluir/<index>', methods=['GET', 'POST'])
def admin_excluir_partida(index):
    if not 'usuario' in session:
       return redirect('/entrar')
    else:
        index_corrigido = int(index)
        partida = PARTIDAS[index_corrigido]
        validacao = excluir_partida(partida)
        if validacao == True:
            return redirect('/admin/partida')
        else:
            return redirect('/')


@admin_bp.route('/admin/partida/alterar/<index>', methods=['GET', 'POST'])
def admin_alterar_partida(index):
    if not 'usuario' in session:
       return redirect('/entrar')
    else:
        erros = []
        index_corrigido = int(index)
        partida = PARTIDAS[index_corrigido]
        if request.method == 'POST':
            form = request.form
            erros = alterar_partida(partida,
                form.get('partida-equipe_casa'), form.get('partida-equipe_visita'),form.get('partida-pontos_casa'), form.get('partida-pontos_visita'))
            if len(erros) == 0:
                return redirect('/admin/partida')

        return render_template('admin/partida_form.html', partidas=PARTIDAS, erros=erros, equipes=EQUIPES, index=index_corrigido)


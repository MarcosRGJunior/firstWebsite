from dados import *


def listar_partida():
    lista = []

    for equipe in EQUIPES:
        pontos = 0
        vitoria = 0
        derrota = 0
        empate = 0
        numero_partidas = 0
        for partida in PARTIDAS:
            if equipe.nome == partida.equipe_casa.nome:
                pontos += obter_pontos(equipe, partida)
                vitoria += obter_vitoria(equipe, partida)
                derrota += obter_derrota(equipe, partida)
                empate += obter_empate(equipe, partida)
                numero_partidas +=1
            elif equipe.nome == partida.equipe_visita.nome:
                pontos += obter_pontos_visita(equipe, partida)
                vitoria += obter_vitoria_visita(equipe, partida)
                derrota += obter_derrota_visita(equipe, partida)
                empate += obter_empate_visita(equipe, partida)
                numero_partidas +=1

        dicionario = {'equipe': equipe.nome, 'sigla': equipe.sigla, 'ponto': pontos,
                      'vitoria': vitoria, 'derrota': derrota,
                      'empate': empate, 'partidas':numero_partidas}

        lista.append(dicionario) 
    
    lista = sorted(lista, key=lambda k: (k['ponto'],k['vitoria'],k['empate']), reverse=True)
    return lista


def obter_pontos(equipe, partida):
    pontos = 0
    if partida.pontos_casa > partida.pontos_visita:
        pontos += 3
    elif partida.pontos_casa == partida.pontos_visita:
        pontos += 1
    else:
        pontos += 0

    return pontos


def obter_vitoria(equipe, partida):
    vitoria = 0
    if partida.pontos_casa > partida.pontos_visita:
        vitoria += 1
    else:
        vitoria += 0

    return vitoria


def obter_derrota(equipe, partida):
    derrota = 0
    if partida.pontos_casa < partida.pontos_visita:
        derrota += 1
    else:
        derrota += 0

    return derrota


def obter_empate(equipe, partida):
    empate = 0
    if partida.pontos_casa == partida.pontos_visita:
        empate += 1
    else:
        empate += 0

    return empate


def obter_pontos_visita(equipe, partida):
    pontos = 0
    if partida.pontos_casa < partida.pontos_visita:
        pontos += 3
    elif partida.pontos_casa == partida.pontos_visita:
        pontos += 1
    else:
        pontos += 0

    return pontos


def obter_vitoria_visita(equipe, partida):
    vitoria = 0
    if partida.pontos_casa < partida.pontos_visita:
        vitoria += 1
    else:
        vitoria += 0

    return vitoria


def obter_derrota_visita(equipe, partida):
    derrota = 0
    if partida.pontos_casa > partida.pontos_visita:
        derrota += 1
    else:
        derrota += 0

    return derrota


def obter_empate_visita(equipe, partida):
    empate = 0
    if partida.pontos_casa == partida.pontos_visita:
        empate += 1
    else:
        empate += 0

    return empate


def obter_resultado(sigla):
    resultados = []
    partidas = obter_partida_equipe(sigla)
    for partida in partidas:
        if partida.equipe_casa.sigla == sigla:
            if partida.pontos_casa > partida.pontos_visita:
                resultado = 'VITORIA'
            elif partida.pontos_casa == partida.pontos_visita:
                resultado = 'EMPATE'
            else:
                resultado = 'DERROTA'
        if partida.equipe_visita.sigla == sigla:
            if partida.pontos_casa < partida.pontos_visita:
                resultado = 'VITORIA'
            elif partida.pontos_casa == partida.pontos_visita:
                resultado = 'EMPATE'
            else:
                resultado = 'DERROTA'

        resultados.append(resultado)
    return resultados


def obter_equipe(sigla):
    lista_equipes = []
    for equipe in EQUIPES:
        dicionario = {'nome': equipe.nome,
                      'sigla': equipe.sigla, 'local': equipe.local}
        lista_equipes.append(dicionario)

    for eqp in lista_equipes:
        if eqp['sigla'] == sigla:
            return eqp

    return {'nome': None,
            'sigla': None, 'local': None}


def obter_partida_equipe(sigla=''):
    equipe = obter_equipe(sigla)
    lista_partida_equipe = []

    for partida in PARTIDAS:
        if partida.equipe_casa.sigla == equipe['sigla'] or equipe['sigla'] == partida.equipe_visita.sigla:
            lista_partida_equipe.append(partida)

    return lista_partida_equipe


def validar_user(login, senha):
    validacao = False
    for usuario in USUARIOS:
        if usuario.email == login:
            if usuario.senha == senha:
                validacao = True

    return validacao


def excluir_equipe(sigla):
    equipe_excluida = obter_equipe(sigla)
    print(equipe_excluida)

    for equipe in EQUIPES:
        if equipe.sigla == equipe_excluida['sigla']:
            lista_partidas = obter_partida_equipe(sigla)
            for partida in lista_partidas:
                PARTIDAS.remove(partida)
            EQUIPES.remove(equipe)
            return True


def excluir_partida(partida_escolhida):
    PARTIDAS.remove(partida_escolhida)
    return True


def incluir_equipe(nome, sigla, local):
    erros = []

    if not sigla:
        erros.append('Sigla é de preenchimento Obrigatório')
    else:
        equipe = obter_equipe(sigla)
        if equipe['sigla'] == sigla:
            erros.append(f'Sigla {sigla} já em uso')

    if not nome:
        erros.append('Nome é de preenchimento Obrigatório')
    else:
        equipe = obter_equipe(sigla)
        if equipe['sigla'] == sigla:
            erros.append(f'Nome {nome} já em uso')

    if not local:
        erros.append('Local é de preenchimento Obrigatório')

    if len(erros) == 0:
        EQUIPES.append(Equipe(nome, sigla, local))
    return erros


def alterar_equipe(nome, sigla_antiga, sigla_nova, local):
    erros = []
    equipe_alterada = obter_equipe(sigla_antiga)

    if not sigla_nova:
        erros.append('Sigla é de preenchimento Obrigatório')
    else:
        equipe = obter_equipe(sigla_antiga)
        if equipe['sigla'] == sigla_nova:
            erros.append(f'Sigla {sigla_nova} já em uso')

    if not nome:
        erros.append('Nome é de preenchimento Obrigatório')
    else:
        equipe = obter_equipe(sigla_antiga)
        if equipe['sigla'] == sigla_nova:
            erros.append(f'Nome {nome} já em uso')

    if not local:
        erros.append('Local é de preenchimento Obrigatório')

    if len(erros) == 0:

        for equipe in EQUIPES:
            print('Nome da equipe: ', equipe)
            print('Equipe sigla: ', equipe.sigla)
            print('Equipe para alterar: ', equipe_alterada['sigla'])
            if equipe.sigla == equipe_alterada['sigla']:
                equipe.nome = nome
                equipe.sigla = sigla_nova
                equipe.local = local

                print('Nome Alterado: ', equipe.nome)
                print('Equipe Alterado: ', equipe.sigla)
                print('Local Alterado: ', equipe.local)

    return erros


def incluir_partida(equipe_casa, equipe_visita, pontos_casa_nova, pontos_visita_nova):
    erros = []
    equipe_casa_correta = None
    equipe_visita_correta = None
    for equipe in EQUIPES:
        if equipe_casa == f'{equipe.nome} ({equipe.sigla})':
            equipe_casa_correta = equipe
        if equipe_visita == f'{equipe.nome} ({equipe.sigla})':
            equipe_visita_correta = equipe

    try:
        pontos_casa = int(pontos_casa_nova)
    except ValueError:
        erros.append('Tipo não aceito, digite um numero')

    try:
        pontos_visita = int(pontos_visita_nova)
    except ValueError:
        erros.append('Tipo não aceito, digite um numero')

    if not equipe_casa:
        erros.append('Equipe Casa é de preenchimento Obrigatório')
    if not equipe_visita:
        erros.append('Equipe Visita é de preenchimento Obrigatório')

    if not pontos_casa_nova:
        erros.append('Pontos Casa é de preenchimento Obrigatório')

    if not pontos_visita_nova:
        erros.append('Pontos Visita é de preenchimento Obrigatório')

    if len(erros) == 0:
        PARTIDAS.append(Partida(equipe_casa_correta, equipe_visita_correta,
                                pontos_casa, pontos_visita))
    return erros


def alterar_partida(partida, equipe_casa_nova, equipe_visita_nova, pontos_casa_nova, pontos_visita_nova):
    erros = []
    obj_equipe_casa = None
    obj_equipe_visita = None

    for equipe in EQUIPES:
            if equipe_casa_nova == f'{equipe.nome} ({equipe.sigla})':
                obj_equipe_casa = equipe
            if equipe_visita_nova == f'{equipe.nome} ({equipe.sigla})':
                obj_equipe_visita = equipe

    try:
        pontos_casa = int(pontos_casa_nova)
    except ValueError:
        erros.append('Tipo não aceito, digite um numero')

    try:
        pontos_visita = int(pontos_visita_nova)
    except ValueError:
        erros.append('Tipo não aceito, digite um numero')
        
    if not equipe_casa_nova:
        erros.append('Equipe Casa é de preenchimento Obrigatório')
    if not equipe_visita_nova:
        erros.append('Equipe Visita é de preenchimento Obrigatório')
    if not pontos_casa_nova:
        erros.append('Pontos Casa é de preenchimento Obrigatório')
    if not pontos_visita_nova:
        erros.append('Pontos Visita é de preenchimento Obrigatório')


    if len(erros) == 0:

        partida.equipe_casa = obj_equipe_casa
        partida.equipe_visita = obj_equipe_visita 
        partida.pontos_casa = pontos_casa_nova
        partida.pontos_visita = pontos_visita_nova
    return erros

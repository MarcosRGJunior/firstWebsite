from classes import Equipe, Partida, Usuario

EQUIPES = [
    Equipe ('Curitiba Vôlei','CVV','Curitiba - PR'),
    Equipe ('Pinheiros','PIV','São Paulo - SP'),
    Equipe ('Brasília Vôlei','BVV','Taguatinga - DF'),
    Equipe ('Vôlei Valinhos','VVV','Valinhos - SP'),
    Equipe ('Vôlei Bauru','VBV','Bauru - SP'),
    Equipe ('Barueri','BRV','Barueri - SP'),
    Equipe ('Praia Clube','PCV','Uberlândia - MG'),
    Equipe ('São Caetano','SCV','São Caetano do Sul - SP'),
    Equipe ('Fluminense','FLV','Rio de Janeiro - RJ'),
    Equipe ('Minas','MIV','Belo Horizonte - MG'),
    Equipe ('Osasco','OSV','Osasco - SP'),
    Equipe ('Rio de Janeiro','RJV','Rio de Janeiro - RJ')
]
PARTIDAS = [
    Partida(EQUIPES[0], EQUIPES[1], 40, 0),
    Partida(EQUIPES[1], EQUIPES[0], 11,  12),
    Partida(EQUIPES[0], EQUIPES[2], 3, 3),
    Partida(EQUIPES[2], EQUIPES[0], 5, 3),
    Partida(EQUIPES[0], EQUIPES[3], 5, 5),
    Partida(EQUIPES[3], EQUIPES[0], 5, 3),
    Partida(EQUIPES[0], EQUIPES[4], 3, 5),
    Partida(EQUIPES[4], EQUIPES[0], 3, 3),
    Partida(EQUIPES[0], EQUIPES[1], 50, 75),
    Partida(EQUIPES[2], EQUIPES[3], 75, 75),
    Partida(EQUIPES[5], EQUIPES[4], 75, 25),
    Partida(EQUIPES[6], EQUIPES[7], 75, 00),
    Partida(EQUIPES[9], EQUIPES[8], 75, 75),
    Partida(EQUIPES[1], EQUIPES[11], 50, 75),
    Partida(EQUIPES[0], EQUIPES[4], 25, 75),
    Partida(EQUIPES[11], EQUIPES[0], 00, 00),
    Partida(EQUIPES[9], EQUIPES[2], 50, 75),
    Partida(EQUIPES[7], EQUIPES[9], 25, 75),
    Partida(EQUIPES[6], EQUIPES[8], 75, 50),
    Partida(EQUIPES[11], EQUIPES[8], 75, 50)

]
USUARIOS = [
    Usuario('admin@admin.com', 'admin123*')
]

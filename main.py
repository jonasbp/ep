# EP - Design de Software
# Equipe: Jonas Bonfá Pelegrina e Layne Pereira da Silva
# Data: 16/10/2020

# Cantor mais ouvido enquanto programava (Jonas): Alcione
# Cantor mais ouvido enquanto programava (Layne):



# Importando as funções do arquivo funções.py
import funções as back
import math


fichas_atuais = 10
print("Você tem {0} fichas".format(fichas_atuais))

print("[1] - APOSTAR NO JOGADOR")
print("[2] - APOSTAR NO BANCO" )
print("[3] - APOSTAR NO EMPATE")


# Confere se o usuário digitou o número correto
vencedor_apostado = int(input("Em quem você deseja apostar? digite o número: "))
if vencedor_apostado == 1 or vencedor_apostado == 2 or vencedor_apostado == 3:
    print("APOSTA EM {0} REGISTRADA.".format(vencedor_apostado))
else:
    print("OPERAÇÃO NEGADA")
    vencedor_apostado = int(input("Em quem você deseja apostar? digite o número: "))

# Confere se o saldo é suficiente para a aposta
fichas_apostadas = int(input("Quantas fichas deseja apostar no (vencedor?)"))
if fichas_atuais >= fichas_apostadas:
    print("APOSTA CONFIRMADA: SALDO SUFICIENTE")
else:
    print("APOSTA NEGADA: SALDO INSUFICIENTE")
    fichas_apostadas = int(input("Quantas fichas deseja apostar no (vencedor?)"))

# Distribuição das cartas aos participantes
jogador = (back.sorteia_cartas(2))
banco = (back.sorteia_cartas(2))

# Realiza a conta das cartas
jogador_soma = jogador[0] + jogador[1]
banco_soma = banco[0] + banco[1]
# jogador_soma = 12
# banco_soma = 13

print(jogador_soma)
print(banco_soma)

#Caso a soma das cartas for maior que 10 corrija para somente a unidade
if (jogador_soma >= 10):
    jogador_soma = jogador_soma % 10

if banco_soma >= 10:
    banco_soma = banco_soma % 10


# Caso as cartas já resultem em 8 ou 9
if (jogador_soma == 8 or jogador_soma == 9) or (banco_soma == 8 or banco_soma == 9):
# Caso aposte no empate e o empate ganhe
    if (jogador_soma == 8 or jogador_soma == 9) and (banco_soma == 8 or banco_soma == 9) and (vencedor_apostado == 3):
        print("Uau você votou no empate e empatou")
        fichas_atuais += (fichas_apostadas * 8)
        print("Seu saldo ficou em: {0}".format(fichas_atuais))
        # ADICIONAR AQUI A VOLTA PARA O INÍCIO PARA JOGAR NOVAMENTE


# Caso aposte no jogador e o jogador ganhe
    elif (jogador_soma == 8 or jogador_soma == 9) and (banco_soma != 8 or banco_soma != 9) and (vencedor_apostado == 1):
        print("JOGADOR GANHOU")
        fichas_atuais = fichas_atuais + fichas_apostadas
        print("Seu saldo ficou em: {0}".format(fichas_atuais))
        # ADICIONAR AQUI A VOLTA PARA O INÍCIO PARA JOGAR NOVAMENTE


# Caso aposte no banco e o banco ganhe
    elif (banco_soma == 8 or banco_soma == 9) and (jogador_soma != 8 or jogador_soma != 9) and (vencedor_apostado == 2):
        print("BANCO GANHOU")
        recebe = 0.95 * fichas_apostadas
        recebe_correto = math.floor(recebe)
        fichas_atuais = fichas_atuais + recebe_correto
        print("Seu saldo ficou em: {0}".format(fichas_atuais))
        # ADICIONAR AQUI A VOLTA PARA O INÍCIO PARA JOGAR NOVAMENTE

#Caso aposte em algúem que não ganhou 
    else:
        print("Você perdeu! :(")
        fichas_atuais = fichas_atuais - fichas_apostadas
        print("Você tem : {0}".format(fichas_atuais))
        # ADICIONAR AQUI A VOLTA PARA O INÍCIO PARA JOGAR NOVAMENTE


# Caso não resulte em 6 ou 7 o jogo empata 
if (jogador_soma == 6 or jogador_soma == 7) and (banco_soma == 6 or banco_soma == 7): 
        print("Uau você votou no empate e empatou!")
        fichas_atuais += (fichas_apostadas * 8)
        print("Seu saldo ficou em: {0}".format(fichas_atuais))
        # ADICIONAR AQUI A VOLTA PARA O INÍCIO PARA JOGAR NOVAMENTE
else: 
    print("O jogo continua.")



# EP - Design de Software
# Equipe: Jonas Bonfá Pelegrina e Layne Pereira da Silva
# Data: 16/10/2020

# Cantor mais ouvido enquanto programava (Jonas): Alcione
# Cantor mais ouvido enquanto programava (Layne):



# Importando as funções do arquivo funções.py
import funções as back


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
jogador_soma = 8
banco_soma = 8


if (jogador_soma == 8 or jogador_soma == 9) and (banco_soma == 8 or banco_soma == 9):
    if vencedor_apostado == 3:
        print("Uau você votou no empate e empatou")
        # fichas_atuais += ()
    else:
        print("O jogo empatou e você não votou no empate,boa sorte na próxima :)")

elif jogador_soma == 8 or jogador_soma == 9:
    print("JOGADOR GANHOU")
elif banco_soma == 8 or banco_soma == 8:
    print("BANCO GANHOU")
else:
    print("Continuando")
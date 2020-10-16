# EP - Design de Software
# Equipe: Jonas Bonfá Pelegrina e Layne Pereira da Silva
# Data: 16/10/2020

# Cantor mais ouvido enquanto programava (Jonas): Alcione
# Cantor mais ouvido enquanto programava (Layne):



#Importando as funções do arquivo funções.py
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
    fichas_apostadas   = int(input("Quantas fichas deseja apostar no (vencedor?)"))
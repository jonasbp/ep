# EP - Design de Software
# Equipe: Jonas Bonfá Pelegrina e Layne Pereira da Silva
# Data: 16/10/2020



# Importando as funções do arquivo funções.py
import funções as back
import math
status = True
status2 = True
novamente = True
novaflag = True

fichas_atuais = 10

print("BARALHOS DISPONÍVEIS:")
print("[1] - Para jogar com 1 baralhos")
print("[6] - Para jogar com 6 baralhos")
print("[8] - Para jogar com 8 baralhos")
contador = True

while contador:
    baralhos = int(input("Com quantos baralhos você deseja jogar? : [1/6/8]"))
    if baralhos == 6 or baralhos == 8 or baralhos == 1:
        print("Baralho escolhido,vamos começar o jogo")
        contador = False
    else:
        print("Você digitou errado")



while novamente:
    print("INICIO : Você tem {0} fichas".format(fichas_atuais))

    print("[1] - APOSTAR NO JOGADOR")
    print("[2] - APOSTAR NO BANCO" )
    print("[3] - APOSTAR NO EMPATE")


    # Confere se o usuário digitou o número correto
    vencedor_apostado = int(input("Em quem você deseja apostar? digite o número: "))
    if vencedor_apostado == 1 or vencedor_apostado == 2 or vencedor_apostado == 3:
        print("APOSTA EM {0} REGISTRADA.".format(vencedor_apostado))
    else:
        print("OPERAÇÃO NEGADA")
        vencedor_apostado = int(input("Em quem você deseja apostar? Digite o número: "))

    # Confere se o saldo é suficiente para a aposta
    fichas_apostadas = int(input("Quantas fichas deseja apostar em quem você selecionou?"))
    if fichas_atuais >= fichas_apostadas:
        print("APOSTA CONFIRMADA: SALDO SUFICIENTE")
    else:
        print("APOSTA NEGADA: SALDO INSUFICIENTE")
        fichas_apostadas = int(input("Quantas fichas deseja apostar em quem você selecionou?"))

    # Distribuição das cartas aos participantes
    jogador = (back.sorteia_cartas(2,baralhos))
    banco = (back.sorteia_cartas(2,baralhos))

    # Realiza a conta das cartas
    jogador_soma = jogador[0] + jogador[1]
    banco_soma = banco[0] + banco[1]
   
    # MANIPULANDO O JOGO PARA TESTES
    jogador_soma = 4
    banco_soma = 3

    #Caso a soma das cartas for maior que 10 corrija para somente a unidade
    if (jogador_soma >= 10):
        jogador_soma = jogador_soma % 10

    if banco_soma >= 10:
        banco_soma = banco_soma % 10

    # print("O jogador recebeu: {0}".format(jogador_soma))
    # print("O banco recebeu: {0}".format(banco_soma))

    while status:
        # Caso as cartas já resultem em 8 ou 9
        if (jogador_soma == 8 or jogador_soma == 9) or (banco_soma == 8 or banco_soma == 9):
        # Caso aposte no empate e o empate ganhe
            if (jogador_soma == 8 or jogador_soma == 9) and (banco_soma == 8 or banco_soma == 9) and (vencedor_apostado == 3):
                print("Uau! Você apostou noe empate e empatou!")
                # Comissão da casa para empate
                if baralhos == 1:
                    pagamento = (fichas_apostadas * 8)
                    pagamento_corrigido = pagamento - (pagamento * 0.1575)
                    fichas_atuais += pagamento_corrigido
                elif baralhos == 6:
                    pagamento = (fichas_apostadas * 8)
                    pagamento_corrigido = pagamento - (pagamento * 0.1444)
                    fichas_atuais += pagamento_corrigido
                else:
                    pagamento = (fichas_apostadas * 8)
                    pagamento_corrigido = pagamento - (pagamento * 0.1436)
                    fichas_atuais += pagamento_corrigido

                print("{1}B , Seu novo saldo é: {0}".format(fichas_atuais,baralhos))
                status = False


        # Caso aposte no jogador e o jogador ganhe
            elif (jogador_soma == 8 or jogador_soma == 9) and (banco_soma != 8 and banco_soma != 9) and (vencedor_apostado == 1):
                print("O JOGADOR GANHOU!")
                # Comissão para caso o jogador ganhe
                if baralhos == 1:
                    pagamento = fichas_apostadas
                    pagamento_ok = pagamento - (pagamento * 0.0129)
                    fichas_atuais += pagamento_ok
                elif baralhos == 6:
                    pagamento = fichas_apostadas
                    pagamento_ok = pagamento - (pagamento * 0.0124)
                    fichas_atuais += pagamento_ok
                else:
                    pagamento = fichas_apostadas
                    pagamento_ok = pagamento - (pagamento * 0.124)
                    fichas_atuais += pagamento_ok
                print("{1}B, Seu novo saldo é: {0}".format(fichas_atuais,baralhos))
                status = False


        # Caso aposte no banco e o banco ganhe
            elif (banco_soma == 8 or banco_soma == 9) and (jogador_soma != 8 or jogador_soma != 9) and (vencedor_apostado == 2):
                print("!O BANCO GANHOU!")
                if baralhos == 1:
                    recebe = 0.95 * fichas_apostadas
                    recebe_correto = math.floor(recebe)
                    recebe_correto_ok = recebe_correto - (recebe_correto * 0.0101)
                    fichas_atuais += recebe_correto_ok
                elif baralhos == 6:
                    recebe = 0.95 * fichas_apostadas
                    recebe_correto = math.floor(recebe)
                    recebe_correto_ok = recebe_correto - (recebe_correto * 0.0106)
                    fichas_atuais += recebe_correto_ok
                else:
                    recebe = 0.95 * fichas_apostadas
                    recebe_correto = math.floor(recebe)
                    recebe_correto_ok = recebe_correto - (recebe_correto * 0.0106)
                    fichas_atuais += recebe_correto_ok

                print("{1} B, Seu novo saldo é: {0}".format(fichas_atuais,baralhos))
                status = False

        #Caso aposte em algúem que não ganhou 
            else:
                print("Você perdeu! :(")
                fichas_atuais = fichas_atuais - fichas_apostadas
                print("Você tem: {0},fichas".format(fichas_atuais))
                status = False
                # ADICIONAR AQUI A VOLTA PARA O INÍCIO PARA JOGAR NOVAMENTE
        else:
            status = False
    while status2: 
        # Caso não resulte em 6 ou 7 o jogo empata 
        if (jogador_soma == 6 or jogador_soma == 7) and (banco_soma == 6 or banco_soma == 7): 
                if vencedor_apostado == 3:
                    print("Uau você votou no empate e empatou!")
                    fichas_atuais += (fichas_apostadas * 8)
                    print("Seu novo saldo é: {0}".format(fichas_atuais))
                    status2 = False
                else:
                    print("O jogo empatou e você não votou no empate :(")
                    fichas_atuais -= fichas_apostadas
                    print("Você tem: {0},fichas".format(fichas_atuais))
                    status2 = False

        else: 
            status2 = False
            
        #Caso soma for menor ou igual a 5
    if (jogador_soma == 8 or jogador_soma == 9) or (banco_soma == 8 or banco_soma == 9):
        novaflag = False

    while novaflag:
        # Distribuição da terceira carta
        if jogador_soma <= 5:
            # cartas recebecidas + carta ganhada
            nova_carta_jogador = back.sorteia_cartas(1,baralhos)
            # print("Nova carta: {0}".format(nova_carta_jogador))
            jogador_soma += nova_carta_jogador[0]
            if (jogador_soma >= 10):
                jogador_soma = jogador_soma % 10
            # print("M5 J: NOVA SOMA: {0}".format(jogador_soma))

            #Caso o jogador tenha recebido uma carta
            print("ENTRANDO NA PARTE NOVA")

            #Se a carta do do jogador for 0
            if nova_carta_jogador[0] == 0:
                if banco_soma == 0:
                    recebe3 = True
                elif banco_soma == 1:
                    recebe3 = True
                elif banco_soma == 2:
                    recebe3 = True
                elif banco_soma == 3:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = False
                elif banco_soma == 4:
                    recebe3 = False
                    
            #Se a carta do do jogador for 1
            elif nova_carta_jogador[0] == 1:
                if banco_soma == 0:
                    recebe3 = True
                elif banco_soma == 1:
                    recebe3 = True
                elif banco_soma == 2:
                    recebe3 = True
                elif banco_soma == 3:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = False
                elif banco_soma == 4:
                    recebe3 = False

            #Se a carta do do jogador for 2
            elif nova_carta_jogador[0] == 2:
                if banco_soma == 0:
                    recebe3 = True
                elif banco_soma == 1:
                    recebe3 = True
                elif banco_soma == 2:
                    recebe3 = True
                elif banco_soma == 3:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = False
            #Se a carta do do jogador for 3
            elif nova_carta_jogador[0] == 3:
                if banco_soma == 0:
                    recebe3 = True
                elif banco_soma == 1:
                    recebe3 = True
                elif banco_soma == 2:
                    recebe3 = True
                elif banco_soma == 3:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = False
            #Se a carta do do jogador for 4
            elif nova_carta_jogador[0] == 4:
                if banco_soma == 0:
                    recebe3 = True
                elif banco_soma == 1:
                    recebe3 = True
                elif banco_soma == 2:
                    recebe3 = True
                elif banco_soma == 3:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = True

            #Se a carta do do jogador for 5
            elif nova_carta_jogador[0] == 5:
                if banco_soma == 0:
                    recebe3 = True
                elif banco_soma == 1:
                    recebe3 = True
                elif banco_soma == 2:
                    recebe3 = True
                elif banco_soma == 3:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = True

            #Se a carta do do jogador for 6
            elif nova_carta_jogador[0] == 6:
                if banco_soma == 0:
                    recebe3 = True
                elif banco_soma == 1:
                    recebe3 = True
                elif banco_soma == 2:
                    recebe3 = True
                elif banco_soma == 3:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = True

            #Se a carta do do jogador for 7
            elif nova_carta_jogador[0] == 7:
                if banco_soma == 0:
                    recebe3 = True
                elif banco_soma == 1:
                    recebe3 = True
                elif banco_soma == 2:
                    recebe3 = True
                elif banco_soma == 3:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = True

            #Se a carta do do jogador for 8
            elif nova_carta_jogador[0] == 8:
                if banco_soma == 0:
                    recebe3 = True
                elif banco_soma == 1:
                    recebe3 = True
                elif banco_soma == 2:
                    recebe3 = True
                elif banco_soma == 3:
                    recebe3 = False
                elif banco_soma == 4:
                    recebe3 = False
                elif banco_soma == 4:
                    recebe3 = False

            #Se a carta do do jogador for 9
            elif nova_carta_jogador[0] == 9:
                if banco_soma == 0:
                    recebe3 = True
                elif banco_soma == 1:
                    recebe3 = True
                elif banco_soma == 2:
                    recebe3 = True
                elif banco_soma == 3:
                    recebe3 = True
                elif banco_soma == 4:
                    recebe3 = False
                elif banco_soma == 4:
                    recebe3 = False
            #Entrega ou não carta para o banco
            
            if recebe3 == True:
                print("banco recebeu carta nova")
                # cartas recebecidas + carta ganhada
                nova_carta_banco = back.sorteia_cartas(1,baralhos)
                # print("Nova carta: {0}".format(nova_carta_banco))
                banco_soma += nova_carta_banco[0]
                if banco_soma >= 10:
                    banco_soma = banco_soma % 10
                # print("M5 B: NOVA SOMA: {0}".format(banco_soma))
            else:
                print("Você não receberá nova carta")

        # Caso o jogador não tenha recebido uma carta 
        if jogador_soma >= 6:
            if banco_soma <= 5:
                # cartas recebecidas + carta ganhada
                nova_carta_banco = back.sorteia_cartas(1,baralhos)
                # print("Nova carta: {0}".format(nova_carta_banco))
                banco_soma += nova_carta_banco[0]
                if banco_soma >= 10:
                    banco_soma = banco_soma % 10
                # print("M5 B: NOVA SOMA: {0}".format(banco_soma))
            
        # Caso aposte no empate e o empate ganhe
        if (jogador_soma == 8 or jogador_soma == 9) and (banco_soma == 8 or banco_soma == 9) and (vencedor_apostado == 3):
            print("Uau! Você apostou noe empate e empatou!")
            # Comissão da casa para empate
            if baralhos == 1:
                pagamento = (fichas_apostadas * 8)
                pagamento_corrigido = pagamento - (pagamento * 0.1575)
                fichas_atuais += pagamento_corrigido
            elif baralhos == 6:
                pagamento = (fichas_apostadas * 8)
                pagamento_corrigido = pagamento - (pagamento * 0.1444)
                fichas_atuais += pagamento_corrigido
            else:
                pagamento = (fichas_apostadas * 8)
                pagamento_corrigido = pagamento - (pagamento * 0.1436)
                fichas_atuais += pagamento_corrigido
            print("{1}B, Seu novo saldo é: {0}".format(fichas_atuais,baralhos))
            novaflag = False


        # Caso aposte no jogador e o jogador ganhe
        elif (jogador_soma == 8 or jogador_soma == 9) and (banco_soma != 8 or banco_soma != 9) and (vencedor_apostado == 1):
            print("O JOGADOR GANHOU!")
            # Comissão para caso o jogador ganhe
            if baralhos == 1:
                pagamento = fichas_apostadas
                pagamento_ok = pagamento - (pagamento * 0.0129)
                fichas_atuais += pagamento_ok
            elif baralhos == 6:
                pagamento = fichas_apostadas
                pagamento_ok = pagamento - (pagamento * 0.0124)
                fichas_atuais += pagamento_ok
            else:
                pagamento = fichas_apostadas
                pagamento_ok = pagamento - (pagamento * 0.124)
                fichas_atuais += pagamento_ok
            print("Seu novo saldo é: {0}".format(fichas_atuais))
            novaflag = False


            #A maior carta ganha depois de ter distribuido a 3 carta
            # Começar a seguir regras 3 carta
            
            #jogador ganhou
        elif jogador_soma > banco_soma and (vencedor_apostado == 1):
            print("Jogador ganhou")
            fichas_atuais += fichas_apostadas
            print("Seu novo saldo é: {0}".format(fichas_atuais))
            novaflag = False
            
            #banco ganhou
        elif banco_soma > jogador_soma and (vencedor_apostado == 2):
            print("Banco Ganhou")
            recebe = 0.95 * fichas_apostadas
            recebe_correto = math.floor(recebe)
            fichas_atuais += recebe_correto
            print("Seu novo saldo é: {0}".format(fichas_atuais))
            novaflag = False

            #Empate
        elif jogador_soma == banco_soma and (vencedor_apostado == 3):
            print("Empate")
            fichas_atuais += (fichas_apostadas * 8)
            print("Seu novo saldo é: {0}".format(fichas_atuais))
            novaflag = False

        # Caso aposte no banco e o banco ganhe
        elif (banco_soma == 8 or banco_soma == 9) and (jogador_soma != 8 or jogador_soma != 9) and (vencedor_apostado == 2):
            print("O BANCO GANHOU!")
            if baralhos == 1:
                recebe = 0.95 * fichas_apostadas
                recebe_correto = math.floor(recebe)
                recebe_correto_ok = recebe_correto - (recebe_correto * 0.0101)
                fichas_atuais += recebe_correto_ok
            elif baralhos == 6:
                recebe = 0.95 * fichas_apostadas
                recebe_correto = math.floor(recebe)
                recebe_correto_ok = recebe_correto - (recebe_correto * 0.0106)
                fichas_atuais += recebe_correto_ok
            else:
                recebe = 0.95 * fichas_apostadas
                recebe_correto = math.floor(recebe)
                recebe_correto_ok = recebe_correto - (recebe_correto * 0.0106)
                fichas_atuais += recebe_correto_ok
            print("Seu novo saldo é: {0}".format(fichas_atuais))
            novaflag = False
        # Caso aposte em alguém que não ganhou
        else:
            print("Voce apostou em algém que não ganhou")
            fichas_atuais = fichas_atuais - fichas_apostadas
            novaflag = False

    #validando caso tenha fixas restantes
    if fichas_atuais > 0:
        status = True
        status2 = True
        novaflag = True 
        i = 1
        while i == 1:
            continuar = input("Você deseja continuar jogando? [S/N]")
            if continuar == "N":
                novamente = False
                i = 0
            elif continuar == "S":
                novamente = True
                i = 0
            else:
                print("Digite de forma correta")
    #Caso não tenha fichas restantes o jogo termina        
    else:
        novamente = False

print("OBRIGADO POR JOGAR! ")
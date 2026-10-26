import random

# Dados do jogo

Mapa = [
        [1, 2, 3, 4, 5], 
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
       ]

def mostrar_mapa():
    for linha in Mapa:
        texto= str(linha)
        print(texto.center(60))


def posição_aleatoria_do_tesouro():
    linha= random.randrange(len(Mapa))
    coluna = random.randrange(len(Mapa[0]))
    return linha, coluna


N_tentativas= 0
resp_jogador = 0


# 

print(35*"-*" + "⚔️ #JOGO CAÇA AO TESOURO#".center(50) + 35*"-*")
print(2*"\n")
mostrar_mapa()
print("\n")
print("Vamos começar o jogo!".rjust(40))
print(2*"\n")


X_no_mapa = posição_aleatoria_do_tesouro()



while resp_jogador != X_no_mapa:

    linha_do_jogador = int(input("Escolha a linha do mapa (0 a 4): "))
    coluna_do_jogador = int(input("escolha a coluna do mapa (0 a 4): "))
    
    resp_jogador = linha_do_jogador, coluna_do_jogador
    N_tentativas +=1

    if resp_jogador == X_no_mapa:
        print("Parabens, Você achou o tesouro!")
        print(f"seu numero de tentativas: {N_tentativas}")
        break

    linha_tesouro, coluna_tesouro = X_no_mapa
    distancia = abs(linha_do_jogador - linha_tesouro) + abs(coluna_do_jogador - coluna_tesouro)

    print("\n")
    print("dica")
    if distancia ==1:
        print("o Tesouro está Muito perto""\n")
    elif distancia ==2:
         print("Perto")
    elif distancia >=3: 
         print("um pouco Longe")
    else:
        print("muito longe")

        
        





     
    


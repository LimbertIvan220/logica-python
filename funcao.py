import random

def imprime_matriz(matriz):
    for linha in range(1):
        for coluna in range(3):
            print(matriz[linha][coluna], end=" ")
        print()

while True:
    matriz = [[random.randint(1,10) for coluna in range (3) for linha in range (1)]]
    if matriz [0][0] == matriz[0][1] == matriz [0][2]:
        imprime_matriz(matriz)
        print("Parabens voce ganhou!")
        print("Voce ganhou muita aura!!!!!")
        for sixSeven in range (1, 68):
            print(sixSeven)
    else:
        imprime_matriz(matriz)
        print("Voce perdeu tente novamente")
    continua = input("\n Deseja continuar? [s, n]: ").lower()
    if continua == "n" or continua == "nao" or continua == "não":
        break
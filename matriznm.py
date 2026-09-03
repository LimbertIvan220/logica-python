import random

while True:
    dim_linha = int(input("digite a dim da linha: "))
    dim_coluna = int(input("digite a dim da coluna: "))
    matriz = [[random.randint(1,10) for coluna in range(dim_coluna)] for linha in range(dim_linha)]
    for coluna in range (dim_coluna):
        for linha in range(dim_linha):
            print(matriz[linha][coluna], end=" ")
        print()
    continua = input("deseja continua?[s,n]: ").lower()
    if continua == "n":
        break
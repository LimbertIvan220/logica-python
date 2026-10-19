import random

dim_coluna = int(input("insira a dimensão da coluna que você deseja: "))
dim_linha = int(input("Insira a dimensão da linha que você deseja: "))
matriz_1 = [[random.randint(1,10) for coluna in range(dim_coluna)]for linha in range (dim_linha)]
matriz_2 = [[random.randint(1,10) for coluna in range(dim_coluna)]for linha in range (dim_linha)]

def imprime_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()
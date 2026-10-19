def soma_linha(matriz, num_linha):
    dim_coluna = len(matriz[0])
    soma = 0
    for coluna in range(dim_coluna):
        soma += matriz[num_linha][coluna]
    return soma

imprime_matriz(matriz)
print()
soma = soma_linha(matriz, 0)
print(f"Soma da linha: {soma}")
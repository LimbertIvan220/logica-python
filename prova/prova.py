def addLista(num):
    lista.append(num)
    return lista

lista= [ ]

while True:
    veiculo = input("Coloque o nome do veiculo: ")
    print(f"lista: {addLista(veiculo)}")
    continua = input("Você deseja continuar digitando? [s,n]: ").lower()
    if (continua == "n") or (continua == "não") or (continua == "nao"):
        break
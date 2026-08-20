soma_total = 0
while True:
    valor = float (input("digite o valor da compra: "))
    soma_total += valor
    print(f"O valor parcial é de R${soma_total}")
    continua = input("Deseja continuar executando? [s, n]").lower()
    if (continua == "n") or (continua == "nao") or (continua == "não"):
        break
print(f"O valor total é de R${soma_total}")
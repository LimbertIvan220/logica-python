def classificar_idade():
    idade = int(input("Digite a sua idade: "))
    if idade < 0:
        return "Não é classificável"
    if idade >= 18:
        return "Adulto"
    elif idade >= 13:
        return "Adolescente"
    elif idade >= 4:
        return "Criança"
    else:
        return "Bebê"

# Para testar a função:
resultado = classificar_idade()
print(f"Você é: {resultado}")

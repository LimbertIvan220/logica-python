def calculadora(num1, num2, operador):
    if operador == "+":
        return num1 + num2
    elif operador =="-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        if num2 == 0:
            return "Não é possível dividir por zero!"
        else:
            return num1 / num2
    else:
        return "Erro opção inválida" 

num1 = 10
num2 = 20
operador = "+"
print(f"{num1} + {num2} = {calculadora(num1, num2, operador)}")
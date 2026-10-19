'''
quantidade_notas = int(input("Digite a quantidade de notas que deseja inserir: "))

notas = []
for i in range(quantidade_notas):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

soma_total = 0
for nota in notas:
    soma_total += nota

media_turma = soma_total / quantidade_notas
print("-" * 30)
print(f"Média da turma: {media_turma:.2f}")

if media_turma >= 7.0:
    print("Desempenho da turma: SATISFATÓRIO")
else:
    print("Desempenho da turma: INSATISFATÓRIO")
print("-" * 30
'''

# Miniprojeto: Planilha de Vendas
# Atividade Prática de Python

# Base inicial fornecida pelo enunciado



'''
vendas = [
    [1200, 1500, 1100],  
    [1000, 1300, 1400],  
    [900, 1700, 1600]    
]

print("--- Etapa 1: Exibição Organizada ---")
for i in range(len(vendas)):
    print(f"Vendedor {i}: Mês 0 = R${vendas[i][0]}, Mês 1 = R${vendas[i][1]}, Mês 2 = R${vendas[i][2]}")

print("\n--- Etapa 2: Total por Vendedor ---")
maior_venda_total = 0
melhor_vendedor = 0

for i in range(len(vendas)):
    acumulador_vendedor = 0
    for j in range(len(vendas[i])):
        acumulador_vendedor += vendas[i][j]
    
    print(f"Total vendedor {i}: R$ {acumulador_vendedor}")
    
    if acumulador_vendedor > maior_venda_total:
        maior_venda_total = acumulador_vendedor
        melhor_vendedor = i

print("\n--- Etapa 3: Total por Mês ---")
for j in range(3):
    acumulador_mes = 0  
    for i in range(3):
        acumulador_mes += vendas[i][j]
    print(f"Total mês {j}: R$ {acumulador_mes}")

print("\n--- Etapa 4: Total Geral ---")
total_geral = 0
for i in range(len(vendas)):
    for j in range(len(vendas[i])):
        total_geral += vendas[i][j]
print(f"Total geral da empresa: R$ {total_geral}")

print("\n--- Etapa 5: Melhor Vendedor ---")
print(f"O melhor vendedor é o Vendedor {melhor_vendedor} (Total: R$ {maior_venda_total})")

vendas = [
    [1200, 1500, 1100], 
    [1000, 1300, 1400],  
    [900, 1700, 1600]   
]

print("--- Etapa 1: Exibição Organizada ---")
for i in range(len(vendas)):
    print(f"Vendedor {i}: Mês 0 = R${vendas[i][0]}, Mês 1 = R${vendas[i][1]}, Mês 2 = R${vendas[i][2]}")

print("\n--- Etapa 2: Total por Vendedor ---")
maior_venda_total = 0
melhor_vendedor = 0

for i in range(len(vendas)):
    acumulador_vendedor = 0  

    for j in range(len(vendas[i])):
        acumulador_vendedor += vendas[i][j]
    
    print(f"Total vendedor {i}: R$ {acumulador_vendedor}")
    
    if acumulador_vendedor > maior_venda_total:
        maior_venda_total = acumulador_vendedor
        melhor_vendedor = i

print("\n--- Etapa 3: Total por Mês ---")
for j in range(3):
    acumulador_mes = 0  

    for i in range(3):
        acumulador_mes += vendas[i][j]
    print(f"Total mês {j}: R$ {acumulador_mes}")

print("\n--- Etapa 4: Total Geral ---")
total_geral = 0

for i in range(len(vendas)):
    for j in range(len(vendas[i])):
        total_geral += vendas[i][j]
print(f"Total geral da empresa: R$ {total_geral}")

print("\n--- Etapa 5: Melhor Vendedor ---")
print(f"O melhor vendedor é o Vendedor {melhor_vendedor} (Total: R$ {maior_venda_total})")
'''



'''
def processar_fechamento_caixa(vendas_do_dia):
    total_acumulado = 0.0
    taxa_imposto = 0.10
    
    for valor_venda in vendas_do_dia:
        imposto = valor_venda * taxa_imposto

        total_acumulado += valor_venda + imposto
        
    return total_acumulado

vendas_teste = [100.0, 200.0, 50.0]

resultado = processar_fechamento_caixa(vendas_teste)
print(f"Resultado obtido: {resultado}")
'''
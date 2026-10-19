'''
def bem_vindo(nome):
    return f"Olá {nome} "
    
print(f" {bem_vindo("Carlos")}")
'''
lista = [1,2,3]

def add_lista(num):
    lista.append(num)
    return lista

print(f"Lista: {add_lista(4)}")
produtos = []
def mostrar_menu():
    print("\nMENU")
    print("\n1 - Cadastrar Livro")
    print("2 - Consultar Livro por ID")
    print("3 - Listar todos os livros")
    print("s - Sair do Programa")

def cadastrar_produto():
    id = int(input("\nDigite o ID do Livro: "))
    nome = input("Digite o nome do Livro: ")
    autor = input("Digite o autor do livro: \n")
    editora = input("Digite a editora do livro: ")
    produto = {
        "id":id,
        "nome":nome,
        "autor":autor,
        "editora":editora
    }
    produtos.append(produto)
    print("\nLivro Cadastro com Sucesso\n")

def busca_id(id):
    for produto in produtos:
        if produto["id"] == id:
            print("\nLivro encontrado")
            print(produto)
            return
    print("\nLivro não encontrado")

def listar_livros():
    print("Livros: ")
    for produto in produtos:
        print(f"ID: {produto['id']} | Nome: {produto['nome']} | Autor: {produto['autor']} | Editora: {produto['editora']}")

def menu_escolha(escolha):
    match escolha:
        case "1":
            cadastrar_produto()
        case "2":
            id_produto = int(input("Digite o ID: "))
            busca_id(id_produto)
        case "3":
            listar_livros()
        case "s":
            pass
        case _:
            print("\nOpção inválida! Tente novamente.")

while True:
    mostrar_menu()
    escolha = input("\nDigite a escolha ou [s] para sair: ")
    if escolha.lower() == "s":
        print("\nPrograma Encerrado\n")
        break
    menu_escolha(escolha)
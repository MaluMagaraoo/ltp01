
biblioteca = []


def adicionar_livro(titulo, autor, ano):
    livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano
    }
    biblioteca.append(livro)
    print(f"O livro '{titulo}' foi adicionado com sucesso!")


def listar_livros():
    if biblioteca:
        print("\nLista de livros:")
        for i, livro in enumerate(biblioteca, start=1):
            print(f"{i}. Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
    else:
        print("Nenhum livro cadastrado.")


def buscar_livro(titulo):
    resultado = [livro for livro in biblioteca if titulo.lower() in livro['titulo'].lower()]
    if resultado:
        print("\nLivros encontrados:")
        for livro in resultado:
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
    else:
        print(f"Nenhum livro encontrado com o título '{titulo}'.")


def gerenciar_biblioteca():
    while True:
        print("\n1. Adicionar livro")
        print("2. Listar todos os livros")
        print("3. Buscar livro por título")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano de publicação: ")
            adicionar_livro(titulo, autor, ano)

        elif opcao == '2':
            listar_livros()

        elif opcao == '3':
            titulo = input("Digite o título do livro que deseja buscar: ")
            buscar_livro(titulo)

        elif opcao == '4':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


gerenciar_biblioteca()

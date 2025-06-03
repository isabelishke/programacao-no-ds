# Tupla com coleção de livros
livros = (
    ("Dom Quixote", "Miguel de Cervantes", 1605),
    ("1984", "George Orwell", 1949),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
)

# Lista para armazenar os livros automaticamente
lista_livros = list(livros)

# Função para adicionar um novo livro
def adicionar_livro(titulo, autor, ano):
    global livros, lista_livros
    novo_livro = (titulo, autor, ano)
    livros += (novo_livro,)  # Atualiza a tupla
    lista_livros.append(novo_livro)  # Atualiza a lista

# Função para exibir os livros armazenados
def consultar_livros():
    print("\nLivros na tupla:")
    for livro in livros:
        print(livro)
    
    print("\nLivros na lista:")
    for livro in lista_livros:
        print(livro)

# Teste do programa
adicionar_livro("A Revolução dos Bichos", "George Orwell", 1945)
consultar_livros()

class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nNúmero de páginas: {self.num_paginas}"

# Solicita ao usuário que insira os dados do livro
titulo = input("Digite o título do livro: ")
autor = input("Digite o autor do livro: ")
num_paginas = input("Digite o número de páginas do livro: ")

# Cria um objeto Livro com os dados inseridos
livro = Livro(titulo, autor, num_paginas)

# Exibe a descrição do livro
print("\nDetalhes do livro cadastrado:")
print(livro)

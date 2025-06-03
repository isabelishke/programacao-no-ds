class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def descrever(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos"

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def descrever(self):
        return f"{super().descrever()}, Raça: {self.raca}"

class Gato(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor

    def descrever(self):
        return f"{super().descrever()}, Cor: {self.cor}"

# Cadastro de animais atendidos
animais = [
    Cachorro("Rex", 5, "Labrador"),
    Gato("Mia", 3, "Cinza"),
    Cachorro("Thor", 2, "Bulldog")
]

# Exibindo os dados cadastrados
for animal in animais:
    print(animal.descrever())

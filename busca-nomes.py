# Lista com pelo menos 8 nomes
nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena"]

# Solicita ao usuário uma letra ou sequência de caracteres
sequencia = input("Digite uma letra ou sequência para buscar nos nomes: ").lower()

# Filtra os nomes que contêm a sequência (ignorando maiúsculas/minúsculas)
nomes_filtrados = [nome for nome in nomes if sequencia in nome.lower()]

# Exibe o resultado
if nomes_filtrados:
    print("Nomes encontrados:")
    for nome in nomes_filtrados:
        print("-", nome)
else:
    print("Nenhum nome encontrado com essa sequência.")

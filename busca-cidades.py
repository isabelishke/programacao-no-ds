# a) Lista com pelo menos 8 cidades
cidades = [
    "Curitiba", "São Paulo", "Rio de Janeiro", "Belo Horizonte",
    "Porto Alegre", "Recife", "Salvador", "Manaus"
]

# b) Solicita entrada do usuário
busca = input("Digite uma letra ou sequência de caracteres para buscar: ").lower()

# c) Filtra cidades que contêm a sequência (ignorando maiúsculas/minúsculas)
resultado = [cidade for cidade in cidades if busca in cidade.lower()]

# d) Exibe resultado
if resultado:
    print("\nCidades encontradas:")
    for cidade in resultado:
        print(f"- {cidade}")
else:
    print("\nNenhuma cidade corresponde à sua busca.")

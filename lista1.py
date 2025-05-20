# Solicita o número de elementos da lista
n = int(input("Digite um número inteiro positivo: "))

# Inicializa a lista
lista = []

# Lê os n números inteiros e adiciona na lista
print(f"Digite {n} números inteiros:")
for _ in range(n):
    num = int(input())
    lista.append(num)

# Solicita o número a ser verificado
x = int(input("Digite o número a ser verificado: "))

# Verifica se x está na lista
if x in lista:
    print(f"{x} pertence à lista.")
else:
    print(f"{x} não pertence à lista.")

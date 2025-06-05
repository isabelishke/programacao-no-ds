# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Gera a sequência usando range e exibe os números
print("\nSequência de números de 0 até", numero)
for i in range(numero + 1):
    print(i)

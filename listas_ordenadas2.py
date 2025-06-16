# 1. Lista de nomes de estudantes
estudantes = ["Carlos", "Ana", "Pedro", "Beatriz", "Mariana"]

# Use sort() para ordenar diretamente a lista original em ordem decrescente
estudantes.sort(reverse=True)
print("Estudantes ordenados (decrescente):", estudantes)

# Lista de nomes de estudantes
estudantes = ["Carlos", "Ana", "Pedro", "Beatriz", "Mariana"]

# Ordenação crescente (A → Z)
estudantes_crescente = sorted(estudantes)
print("Ordem crescente:", estudantes_crescente)

# Ordenação decrescente (Z → A)
estudantes_decrescente = sorted(estudantes, reverse=True)
print("Ordem decrescente:", estudantes_decrescente)

# Verificação da lista original
print("Lista original:", estudantes)

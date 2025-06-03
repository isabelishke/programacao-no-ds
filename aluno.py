import functools

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f'{self.nome}: {self.nota}'

def comparar_alunos(a, b):
    return (a.nota > b.nota) - (a.nota < b.nota)

# Coletar dados dos alunos
alunos = []
for i in range(3):
    nome = input(f'Digite o nome do aluno {i + 1}: ')
    while True:
        try:
            nota = float(input(f'Digite a nota de {nome}: '))
            break
        except ValueError:
            print("Por favor, insira uma nota válida (número).")
    alunos.append(Aluno(nome, nota))

# Ordenar os alunos pela nota
alunos_ordenados = sorted(alunos, key=functools.cmp_to_key(comparar_alunos))

# Exibir os alunos ordenados
print("\nAlunos ordenados por nota:")
for aluno in alunos_ordenados:
    print(aluno)

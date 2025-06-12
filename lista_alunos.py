# Lista de alunos com nome e nota
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Carlos", "nota": 9.0},
    {"nome": "Bruno", "nota": 7.8},
    {"nome": "Daniela", "nota": 9.5},
    {"nome": "Eduardo", "nota": 6.7}
]

# Ordenando por nome (modifica a lista original)
alunos.sort(key=lambda aluno: aluno["nome"])

print("Alunos ordenados por nome:")
for aluno in alunos:
    print(f"{aluno['nome']} - {aluno['nota']}")

# Ordenando por nota em ordem decrescente (gera nova lista)
alunos_por_nota = sorted(alunos, key=lambda aluno: aluno["nota"], reverse=True)

print("\nAlunos ordenados por nota (decrescente):")
for aluno in alunos_por_nota:
    print(f"{aluno['nome']} - {aluno['nota']}")

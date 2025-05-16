import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
anos = 10
simulacoes = 10  # Ajuste conforme necessário
retorno_medio = 0.07
desvio_padrao = 0.20
valor_inicial = 10000  # Valor inicial da carteira

# Simulação de Monte Carlo
np.random.seed(42)  # Para reprodutibilidade
trajetorias = np.zeros((anos + 1, simulacoes))
trajetorias[0] = valor_inicial

for i in range(1, anos + 1):
    retornos_anuais = np.random.normal(retorno_medio, desvio_padrao, simulacoes)
    trajetorias[i] = trajetorias[i - 1] * (1 + retornos_anuais)

# Plotando o gráfico
plt.figure(figsize=(10, 5))
plt.plot(trajetorias)
plt.xlabel("Ano")
plt.ylabel("Valor da Carteira (R$)")
plt.title("Simulação de Monte Carlo para Investimentos em Ações")
plt.grid()
plt.show()

class Veiculo:
    def __init__(self, modelo, consumo_por_km, preco_por_litro):
        self.modelo = modelo
        self.consumo_por_km = consumo_por_km  # Litros por km
        self.preco_por_litro = preco_por_litro  # Preço do combustível por litro

    def calcular_custo_viagem(self, distancia):
        return distancia * self.consumo_por_km * self.preco_por_litro

class Carro(Veiculo):
    pass

class Moto(Veiculo):
    pass

class Caminhao(Veiculo):
    pass

# Lista de veículos
veiculos = [
    Carro("Sedan", 0.08, 6.0),    # Consumo: 12,5 km/L
    Moto("Sport", 0.04, 6.0),     # Consumo: 25 km/L
    Caminhao("Carga pesada", 0.25, 6.0) # Consumo: 4 km/L
]

# Calculando o custo total da viagem de 200 km
distancia = 200
custo_total = sum(veiculo.calcular_custo_viagem(distancia) for veiculo in veiculos)

print(f"Custo total da viagem de {distancia} km para todos os veículos: R$ {custo_total:.2f}")

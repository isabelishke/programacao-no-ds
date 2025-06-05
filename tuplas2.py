# Solicita ao usuário as coordenadas geográficas
coordenadas = input("Digite as coordenadas geográficas (latitude, longitude) separadas por vírgula: ")

# Converte a entrada em uma tupla de números float
latitude, longitude = map(float, coordenadas.split(","))

# Exibe as coordenadas extraídas
print("\nCoordenadas Geográficas:")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

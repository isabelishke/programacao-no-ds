def calcular_engajamento():
    print("Calculadora de Engajamento em Redes Sociais")
    
    curtidas = int(input("Digite o número de curtidas: "))
    comentarios = int(input("Digite o número de comentários: "))
    compartilhamentos = int(input("Digite o número de compartilhamentos: "))
    
    seguidores = int(input("Digite o número de seguidores: "))
    alcance = int(input("Digite o alcance da publicação: "))
    impressoes = int(input("Digite o número de impressões: "))
    
    # Cálculo das métricas de engajamento
    engajamento_seguidores = (curtidas + comentarios + compartilhamentos) / seguidores * 100 if seguidores != 0 else 0
    engajamento_alcance = (curtidas + comentarios + compartilhamentos) / alcance * 100 if alcance != 0 else 0
    engajamento_impressoes = (curtidas + comentarios + compartilhamentos) / impressoes * 100 if impressoes != 0 else 0
    
    print("\nResultados:")
    print(f"Engajamento por Seguidores: {engajamento_seguidores:.2f}%")
    print(f"Engajamento por Alcance: {engajamento_alcance:.2f}%")
    print(f"Engajamento por Impressões: {engajamento_impressoes:.2f}%")

# Executar o programa
calcular_engajamento()

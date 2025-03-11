import random  # Importa o módulo 'random', que fornece funções para gerar números pseudoaleatórios.

# Gera um número aleatório entre 1 e 10, que será o número secreto.
numero_secreto = random.randint(1, 10)  
tentativas = 0  # Inicializa o número de tentativas do jogador como 0.
max_tentativas = 5  # Define o número máximo de tentativas permitidas.

# Exibe mensagens introdutórias ao jogador.
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando, entre 1 e 10.")

# Loop principal do jogo, que continuará até que o jogador atinja o limite de tentativas.
while tentativas < max_tentativas:
    # Solicita que o jogador insira um palpite (um número inteiro).
    palpite = int(input("Digite seu palpite: "))

    # Incrementa o contador de tentativas cada vez que o jogador faz um palpite.
    tentativas += 1

    # Verifica se o palpite do jogador está correto.
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")  # Mensagem de sucesso.
        break  # Encerra o loop, pois o jogador venceu o jogo.
    elif palpite < numero_secreto:
        # Sugere que o jogador tente um número maior.
        print("Quase lá! Tente um número maior.")
    else:
        # Sugere que o jogador tente um número menor.
        print("Quase lá! Tente um número menor.")

    # Informa ao jogador quantas tentativas restam, desde que ele ainda tenha tentativas disponíveis.
    if tentativas < max_tentativas:
        print(f"Você tem {max_tentativas - tentativas} tentativas restantes.")

# Esse bloco será executado se o jogador não adivinhar o número no limite de tentativas.
else:
    print("Infelizmente, você não acertou. O número era", numero_secreto)  # Revela o número secreto.
    print("Fim do jogo!")  # Exibe uma mensagem de encerramento.

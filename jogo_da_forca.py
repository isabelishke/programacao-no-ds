def desenha_forca(erros):
    partes = [
        " O ",   # Cabeça
        " | ",   # Corpo
        "/| ",   # Braço esquerdo
        "/|\\",  # Braços completos
        "/  ",   # Perna esquerda
        "/ \\"   # Pernas completas
    ]
    
    print("\n+---+")
    print(f"|   {' ' if erros < 1 else partes[0]}")
    print(f"|   {' ' if erros < 2 else partes[1]}")
    print(f"|  {' ' if erros < 3 else partes[2]}")
    print(f"|  {' ' if erros < 4 else partes[3]}")
    print(f"|  {' ' if erros < 5 else partes[4]}")
    print(f"|  {' ' if erros < 6 else partes[5]}")
    print("===")

def jogar_forca():
    palavra_secreta = "girafa"
    letras_acertadas = ["_"] * len(palavra_secreta)
    tentativas = 6

    while tentativas > 0 and "_" in letras_acertadas:
        print(" ".join(letras_acertadas))
        desenha_forca(6 - tentativas)
        
        palpite = input("Digite uma letra: ").lower()

        if palpite in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if letra == palpite:
                    letras_acertadas[index] = letra
        else:
            tentativas -= 1
            print(f"Você tem {tentativas} tentativas restantes.")
        
    desenha_forca(6 - tentativas)
    
    if "_" not in letras_acertadas:
        print("Parabéns, você ganhou!")
    else:
        print("Que pena, você perdeu. A palavra era:", palavra_secreta)

# Iniciar o jogo
jogar_forca()

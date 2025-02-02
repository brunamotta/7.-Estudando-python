import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print(f"(1) Fácil   (2) Médio   (3) Difícil")

    nivel = int(input("Escolha o nível:"))
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    print(numero_secreto)

    for rodada in range(1,total_tentativas + 1) :
        print(f"Tentativa: {rodada} de {total_tentativas}")

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100) :
            print("você deve digitar um número entre 1 e 100!")
            print(" ")
            continue

        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto

        if (acertou) :
            print(f"Você acertou e fez {pontos} pontos!")
            print(" ")
            break
        else:
            if (maior) :
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos    
        
        rodada += 1
        print(" ")

    print("Fim do Jogo!")

if (__name__ == "__main__"):
    jogar()

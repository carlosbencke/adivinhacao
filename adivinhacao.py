import random
print("====================================")
print("= Bem vindo ao jogo de adivinhação =")
print("====================================")

numero_secreto = random.randrange(1,101)
# print(numero_secreto)
total_de_tentativas = 10

for rodada in range(1, total_de_tentativas + 1):
    # String Interpolation - Insere o valor de .format nas chaves dentro da string.
    print("Tentativa  {} de {} ".format(rodada, total_de_tentativas))
    chute_str = (input("Digite o seu número: "))  # Recebe um input como string
    print("Você chutou ", chute_str)
    chute = int(chute_str)  # Converte o string para integer para poder fazer a comparação no if.

    if chute < 1 or chute > 100:
        print("Você precisa digitar um número entre 1 e 100!")
        continue # Retorna para o início do laço

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:  # Compara dois int e imprime o resultado do jogo.
        print("Você acertou!")
        break # Termina o laço caso a pessoa acerte o número secreto.
    else:
        if menor:
            print("Você errou! O seu chute foi menor do que o número secreto!")
        elif maior:
            print("Você errou O seu chute foi maior do que o número secreto!")


print("====================================")
print("=========== Fim de jogo ============")
print("====================================")

import random
cara_ou_coroa = random.randint(1, 2)
print("1. Cara")
print("2. Coroa")
# print("Resposta: ", cara_ou_coroa) // Para debug
escolha_usuario = int(input("Vai ser cara ou coroa? "))


if (escolha_usuario == cara_ou_coroa):
    print("Parabéns, você acertou!!")
else:
    print("Errou!!")

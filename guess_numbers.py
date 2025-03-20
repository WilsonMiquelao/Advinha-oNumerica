import random

print("Seja muito bem vindo ao Guess Number!")
numero_limite = input("Digite até qual número será a advinhação: ")

if numero_limite.isdigit():
    numero_limite = int(numero_limite)
else:
    print("Erro: valor informado não é um número. Favor executar novamente e informar um numero!")
    quit()

numero_randomico = random.randint(0, numero_limite)

numero_tentativas = 0

while True:
    resposta_usuario = input("Digite um numero para tentar adivinhar: ")

    if resposta_usuario.isdigit():
        resposta_usuario = int(resposta_usuario)
    else:
        print("Erro: valor informado não é numérico. Favor informar um numero!")
        continue
    
    numero_tentativas = numero_tentativas + 1

    if resposta_usuario == numero_randomico:
        print("Acertou!")
        break
    elif resposta_usuario > numero_randomico:
        print("Chutou alto, o numero escolhido é menor que o digitado")
    else: 
        print("Chutou baixo, o numero escolhido é maior que o digitado")

print(f"Você tentou {numero_tentativas} vezes até acertar o número escolhido")


        





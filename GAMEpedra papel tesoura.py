import time 
from random import randint

print("{:=^40}".format(" GAME PEDRA PAPEL E TESOURA "))
opções = print(''' SUAS OPÇÕES 
[ 1 ] PEDRA 
[ 2 ] PAPEL
[ 3 ] TESOURA ''')

jogadas = ["pedra", "papel", "tesoura"]

jogador = int(input(" Qual é a sua jogada? "))
jogador = jogadas[jogador - 1]  # Convertendo o número para a jogada correspondente

computador = randint(1, 3)
computador = jogadas[computador - 1]  # Convertendo o número do computador para a jogada correspondente
time.sleep(1) # delay de 1 segundo
print(" JO ")
time.sleep(1)
print(" KEN ")
time.sleep(1)
print(" PO!!! ")

if (jogador == "pedra" and computador == "tesoura") or \
   (jogador == "papel" and computador == "pedra") or \
   (jogador == "tesoura" and computador == "papel"):
    print("Você venceu!")
else:
    print("Você perdeu!")

print("{:=^30}".format(""))
print("Computador jogou", computador)
print("Jogador jogou", jogador)
print("{:=^30}".format(""))

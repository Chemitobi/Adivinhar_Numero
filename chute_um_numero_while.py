import random
import os

controle_final ="s"
while controle_final== "s":

    print("====================NEW GAME=====================")

    num = random.randint(1,10)
    controle ="s"

    while controle == "s":
        num_usuario = int(input('Digite um número de 1 a 10: '))

        if num_usuario == num:
            print('$$$$$$$$$$$$Você venceu!!!$$$$$$$$$$$$$$')
            controle ="n"

        else:
            print('Não foi desta vez!!')

        if num_usuario > num:
            print("O número que você escolheu é maior que o numero do computador!!!")

        elif num_usuario < num:
            print("O número que você escolheu é menor que o número do computador!!!")

    controle_final = input("Deseja Jogar outra vez? [s] ou [n]:")
    
    os.system("clear")
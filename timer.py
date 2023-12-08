import time

while True:

    num = input("Digite o tempo em segundos: ")

    if num.isdigit():
        num = int(num)
        break
    else:
        print("Opção invalida, tente novamente!")

for x in range(num, 0, -1):
    segundos = x % 60
    minutos = int(x / 60) % 60
    horas = int(x / 3600)
    timer = (f"{horas:02}:{minutos:02}:{segundos:02}")
    print(timer, end="\r")
    time.sleep(1)

print('Tempo Esgotado!')
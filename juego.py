import random

numero_aleatorio = random.randint(0,5)

while True:
    numero = int(input("Ingresa el numero que estoy pensando, cual tienes?"))
    if numero_aleatorio==numero:
        break
    
print("Adivinaste el numero!!!")
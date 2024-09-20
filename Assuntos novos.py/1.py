import os 
os.system (" cls || clear")

numeros_inseridos = []
numeros_negativos = []
numeros_positivos = []

for i in range (5):
    numeros = int (input (f"Digite o seu numero {i+1}:  "))
    numeros_inseridos.append(numeros)

    if numeros < 0 :
        numeros_negativos.append(numeros)

    else:
        numeros_positivos.append(numeros)


print (f"Os seus números inseridos foram: {numeros_inseridos}")
print (f"Os seus números inseridos positivos foram: {numeros_positivos}")
print (f"Os seus números inseridos negativos foram: {numeros_negativos}")



import os 
os.system("clls| clear")

# Declaração de variáveis.

notas = 3
calculo = 0 

# Solicitando Dados.

for i in range (3):
    while True :    
        notas = float (input  ( f"Digite a sua nota {i + 1} : "))

        if notas < 0 or notas > 10:
            print("Nota é invalida ")
        else : 
            # Calculo.
            calculo += notas
            break

media = calculo /3             

#Exibição de resultado

if media  >7 :
    print ("Você passou !")
    
elif media <=4 :
    print ("Você está reprovado ! ")
    
else : 
    print ("Você está de recuperação!")
    

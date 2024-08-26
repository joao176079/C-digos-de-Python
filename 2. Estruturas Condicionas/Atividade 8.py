import os 
os.system("clls| clear")

print (" Dias da semana")
print ("""
1- Domingo
2- Segunda
3- Terça
4- Quarta
5- Quinta
6- Sexta 
7- Sabado""")

opcao = int (input (" Digite a sua opção : "))
match (opcao):
    case 1:
        print("Você escolheu domingo final de semana !")
    case 2:
        print ("Você escolheu segunda !")
    case 3:
        print ("Você escolheu terça !")
    case 4:
        print ("Você escolheu  quarta ! ")
    case 5 :  
        print ("Você escolheu quinta ! ")
    case    6:
        print ("Você escolheu sexta ! ")
    case 7 :
        print ("Você escolheu sabado final de semana !")
    case "_" :
        print ("Invalido")

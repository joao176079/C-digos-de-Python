import os 
os.system("clls| clear")

print (" Mêses do ano")
print ("""
1-  Janeiro 
2-  Fevereiro 
3-  Março
4-  Abril
5-  Maio
6-  Junho
7-  Julho 
8-  Agosto
9-  Setembro
10- Outubro
11- Novembro 
12- Dezembro       """)

opcao = int (input (" Digite a sua opção : "))
match (opcao):
    case 1:
        print("Você escolheu Janeiro  !")
    case 2:
        print ("Você escolheu Fevereiro  !")
    case 3:
        print ("Você escolheu Março !")
    case 4:
        print ("Você escolheu Abril  ! ")
    case 5 :  
        print ("Você escolheu Maio ! ")
    case    6:
        print ("Você escolheu Junho ! ")
    case 7 :
        print ("Você escolheu Julho !")
    case 8 :
        print ("Você escolheu Agosto !")
    case 9 :
        print (" Você escolheu Setembro ! ")
    case 10 :
        print (" Você escolheu Outubro !")
    case 11 :
        print (" Você escolheu Novembro !")
    case 12 : 
        (" Você escolheu Dezembro ! ")
    

import os 
os.system("clls| clear")

#Solicitando dados .
soma = 0 
contador = 0 

#Execução do programa 

while True :

    nota = float (input ( " Digite uma nota: "))
    contador += 1 
    soma += nota
    resposta = input ( " Deseja inserir mais uma nota ? ").upper()
    

    if resposta == 'n':
        break

    media = soma / contador 
    print (f"Media:" , media)
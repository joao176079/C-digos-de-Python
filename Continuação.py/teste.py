import os 
os.system("clls| clear")


#lista_produtos = [ "chocolate ","miojo" , 'macarrão ']
#for produto in lista_produtos :
   # print (produto.capitalize())

#lista_preco = [ 10 , 20 , 30 ]
#for preco in lista_preco :
 #   print ( preco )

# Solicitando dados. 


soma  = 0
resultado = 0

for i in range (5): 
    
    numero = int ( input (f" Digite o {i+1} número : "))
    
    soma = soma + numero 

print (f"Soma  : {soma} ")

pares=0
impares=0

for i in range ( 5) :
    numero = int (input (" Digite um número: " ))

    if numero % 2 == 0 :
        pares = pares + 1

    else :
        impares = impares + 1
print (f"Quantidade de pares : {pares} ")
print (f"Quantidade de impares : {impares} ")
















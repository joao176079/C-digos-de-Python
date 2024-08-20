import os 
os.system("clls| clear")

# Solicitando dados.

nome = str (input (" Digite seu nome: "))
idade = int (input ( " Digite sua idade: "))
nota1 = int ( input ( " Digite sua primeira nota: "))
nota2 = int ( input (" Digite sua segunda nota:"))
nota3 = int ( input (" Digite sua terceira nota:"))
resultado = (nota1 + nota2 + nota3) / 3


# Exibindo Dados 

print (f" Nome: {nome} ")
print (f" Idade: {idade} ")
print (f" Nota1: {nota1}")
print (f" Nota 2: {nota2}")
print (f" Nota 3: {nota3}")


# Calculo 

if resultado < 7 :
    print (" Você foi reprovado ")
else :
    print (" Você foi aprovado ")

import os 
os.system("clls| clear")

numero1 = int (input ( " Digite o seu primeiro número: "))
numero2 = int (input ( " Digite o seu segundo número:"))

soma = numero1 + numero2
produto = numero1*numero2
media = (numero1 + numero2) /2

print (f" A soma de {numero1} e {numero2} é : {soma}")
print (f" A media de {numero1} e {numero2} é de : {media}")
print (f" O produto de {numero1} e {numero2} é : {produto}")

if numero1< numero2 :
    print (" \nO número 2 é maior e o número 1 é menor")
else :
    print ("\nO número 1 é maior e o  número 2 é menor ")
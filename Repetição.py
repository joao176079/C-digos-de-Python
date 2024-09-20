#import os 
#os.system("clls| clear")

#nota = float (input (" Digite a sua nota : "))
#while nota < 0 or nota > 10: 
#    nota = float ( input (" insira entre 0 a 10 :"))
#print (f"Sua nota foi {nota}")

import os
os.system("cls || clear")

novologin = input("Digite seu novo login: ")
novasenha = input("Digite sua nova senha: ")

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")


while True :
      if login != novologin and novasenha != senha:
             print("senha ou login incorretos")
             break
      else: 
       print ("Bem vindo")
       break
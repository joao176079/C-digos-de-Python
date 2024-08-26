import os 
os.system("clls| clear")



print("Bem vindo a calculadora!")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print ("""
+ para adição 
- para subtração
* para multiplicação
/ para divisão
""")
opcao = input("escolha a opção ")

match (opcao):
    case "+":
        print("O resultado foi: ")
        print( num1 + num2)
    case "-":
        print("O resultado foi: ")
        print(num1 - num2)
    case "*":
        print("O resultado foi: ")
        print(num1 * num2)
    case "/":
        print("O resultado foi: ")
        print(num1 / num2)
    case _ :  
        print("Error 1")


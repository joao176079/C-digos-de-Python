 
print (""" 
Digite 1 - Caso seja masculino  | Digite 2 - Caso seja feminino""" )

altura = float (input (" Qual sua altura : "))
opcao = int(input (" Digite sua opção : "))

match (opcao):
    case 2 :
        feminino = (62.1 *  altura) - 58
        print (f" Sua altura é igual a {feminino:.2f}")
    case 1 :
        masculino =  (72.7 * altura) - 44.7
        print (f" A sua altura é igual a {masculino:.2f}")
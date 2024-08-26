import os 
os.system("clls| clear")

escolha_a_forma_de_pagamento =  int (input (""" Digite  a forma de pagamento :
 1- Pagamento a vista. | 2- Pagamento a prazo: """)  )                                   
valor_produto=  int (input (" Digite o seu valor :"))


match ( escolha_a_forma_de_pagamento):
    case 1 : 
        desconto =  0.10 * valor_produto
        valor_com_desconto = valor_produto - desconto
        print (f" Total a pagar :{valor_com_desconto}")
        
    case 2 :
        parcela = int ( input ( " Digite a quantidade de parcelas que você tem que pagar "))
        




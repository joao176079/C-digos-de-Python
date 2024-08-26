import os 
os.system("clls| clear")
soma = 0
resultado = 0

print("Coloque as suas notas , e ao final ira vir a média. ")



for i in range (4): 
    
    numero = int ( input (f" Digite a sua primeiro nota  {i+1} : "))
    
    soma = soma + numero
    resultado = (soma + numero) /  4
    
print (f"Soma  : {resultado} ")
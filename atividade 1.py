import os 
os.system("clls| clear")
soma = 0
media = 0

print("Coloque as suas notas , e ao final ira vir a média. ")



for i in range (3): 
    
    numero = int ( input (f" Digite a sua primeiro nota  {i+1} : "))
    
    soma = soma + numero
    media = (soma + media) /  4
    
print (f"Nota : {media:.1f} ")

if media >7 :
    print ("O aluno está aprovado. ")
elif media >= 4 :
    print ("O aluno está de recuperação. ")
else :
    print ("O aluno está reprovado. ")
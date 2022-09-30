'''
Construa um algoritmo que receba como entrada três valores e os imprima em
ordem crescente.
'''

n1=int(input("Insira aqui o primeiro numero: "))
n2=int(input("Insira aqui o segundo numero: "))
n3=int(input("Insira aqui o terceiro numero: "))

if n1>=n2 and n1>n3:
    if n2>=n3:
        print(n3,", ",n2," e ",n1)
    else:
        print(n2,", ",n3," e ",n1)
    
elif n2>n1 and n2>=n3:
    if n1>=n3:
        print(n3,", ",n1," e ",n2)
    else: 
        print(n1,", ",n3," e ",n2)
elif n3>=n1 and n3>n2:
    if n1>=n2:
        print(n2,", ",n1," e ",n3)
    else:
        print(n1,", ",n2," e ",n3)
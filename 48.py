'''
Faça um algoritmo que leia 3 números inteiros distintos e escreva o menor deles.
'''


a=float(input("Insira aqui o primeiro numero: "))
b=float(input("Insira aqui o primeiro numero: "))
c=float(input("Insira aqui o primeiro numero: "))

if(a>b and a>c):
    if (b>c):
        print(c)
    elif (b<c):
        print(b)

if(b>c and b>a):
    if (c>a):
        print(a)
    elif (c<a):
        print(c)

if (c>a and c>b):
    if (a>b):
        print(b)
    elif (a<b):
        print(a)
        
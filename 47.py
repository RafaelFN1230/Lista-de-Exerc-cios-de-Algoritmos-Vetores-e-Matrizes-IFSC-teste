'''
Construir um algoritmo que tome como entradas três valores distintos e os
apresente (imprima) em ordem crescente (menor para o maior).
'''

a=float(input("Insira aqui o primeiro numero: "))
b=float(input("Insira aqui o primeiro numero: "))
c=float(input("Insira aqui o primeiro numero: "))

if(a>b and a>c):
    if (b>c):
        print(a,"",b,"",c)
    elif (b<c):
        print(a,"",c,"",b)

if(b>c and b>a):
    if (c>a):
        print(b,"",c,"",a)
    elif (c<a):
        print(b,"",a,"",c)

if (c>a and c>b):
    if (a>b):
        print(c,"",a,"",b)
    elif (a<b):
        print(c,"",b,"",a)
        
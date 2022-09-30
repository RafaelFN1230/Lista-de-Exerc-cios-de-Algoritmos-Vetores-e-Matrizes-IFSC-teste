'''
Faça um algoritmo que leia dois números e indique se são iguais ou se são
diferentes. Mostre o maior e o menor (nesta sequência).
'''

n_1=float(input("Insira aqui o primeiro numero: "))
n_2=float(input("Insira aqui o segundo numero: "))

if(n_1!=n_2):
    print("Os dois numeros são diferentes.")
    if (n_1>n_2):
        print("O primeiro numero é maior.")
    else:
        print("O segundo numero é maior")
else:
    print("Os dois numeros são iguais.")
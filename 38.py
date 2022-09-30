'''
Faça um algoritmo que leia os valores A, B e C. Mostre uma mensagem que
informe se a soma de A com B é menor, maior ou igual a C.
'''

A=float(input("Insira o valor de A:"))
B=float(input("Insira o valor de B:"))
C=float(input("Insira o valor de C:"))


if A+B>C:
    print("MAIOR")
elif A+B<C:
    print("MENOR")
else:
    print("IGUAL")
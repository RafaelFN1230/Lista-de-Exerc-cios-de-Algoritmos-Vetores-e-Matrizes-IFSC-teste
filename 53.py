'''
Faça um algoritmo que leia três números e mostre-os em ordem decrescente.
'''

n_1=float(input("Insira aqui o primeiro numero: "))
n_2=float(input("Insira aqui o segundo numero: "))
n_3=float(input("Insira aqui o terceiro numero: "))

if (n_1>n_2 and n_1>n_3):
    if (n_2>n_3):
        print(n_1,"é maior do que ",n_2,"é maior do que",n_3)
    elif (n_3>n_2):
        print(n_1,"é maior do que ",n_3,"é maior do que",n_2)
    else:
        print(n_1,"é maior do que ",n_3,"é igual",n_2)

elif (n_2>n_1 and n_2>n_3):
    if (n_1>n_3):
        print(n_2,"é maior do que ",n_1,"é maior do que",n_3)
    elif (n_3>n_1):
        print(n_2,"é maior do que ",n_3,"é maior do que",n_1)
    else:
        print(n_2,"é maior do que ",n_3,"é igual",n_1)

elif (n_3>n_2 and n_3>n_1):
    if (n_2>n_1):
        print(n_3,"é maior do que ",n_2,"é maior do que",n_1)
    elif (n_1>n_2):
        print(n_3,"é maior do que ",n_1,"é maior do que",n_2)
    else:
        print(n_2,"é maior do que ",n_3,"é igual",n_1)

elif (n_1==n_2 and n_2==n_3):
    print("Os tres numeros são iguais.")
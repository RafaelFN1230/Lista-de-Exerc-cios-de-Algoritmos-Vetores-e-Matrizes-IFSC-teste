'''
Faça um algoritmo que leia um número N e imprima “F1”, “F2” ou “F3”, conforme
a condição:
• “F1”, se N <= 10
• “F2”, se N > 10 e N <= 100
• “F3”, se n > 100
'''

N=float(input("Insira aqui um numero: "))
if N<=10:
    print("F1")
elif N>10 and N<=100 :
    print("F2")
else:
    print("F3")
    
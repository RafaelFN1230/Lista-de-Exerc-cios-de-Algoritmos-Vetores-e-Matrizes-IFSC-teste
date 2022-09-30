'''
Um hotel cobra R$ 60.00 a diária e mais uma taxa de serviços. A taxa de
serviços é de:
• R$ 5.50 por diária, se o número de diárias for maior que 15;
• R$ 6.00 por diária, se o número de diárias for igual a 15;
• R$ 8.00 por diária, se o número de diárias for menor que 15.
Construa um algoritmo que mostre o nome e o total da conta de um cliente.
'''

nome=input("Insira o nome do cliente: ")
diaria=60
n_diaria=int(input("Insira o numero de diárias: "))
if (n_diaria>15):
    total=(diaria+5.50)*n_diaria
elif(n_diaria==15):
    total=(diaria+6)*n_diaria
elif(n_diaria<15):
    total=(diaria+8)*n_diaria

print(nome, "seu total é de: R$%.2f" %total)
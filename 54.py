'''
Faça um algoritmo que leia quatro números (Opção , Num1 , Num2 e Num3) e
mostre o valor de Num1 se Opção for igual a 2; o valor de Num2 se Opção for
igual a 3; e o valor de Num3 se Opção for igual a 4. Os únicos valores possíveis
para a variável Opção são 2, 3 e 4.
'''

opcao=int(input("Insira a opção(2, 3 ou 4): "))
num1=int(input("Insira o Prmeiro numero: "))
num2=int(input("Insira o Segundo numero: "))
num3=int(input("Insira o Terceiro numero: "))
if(opcao==2):
    print(num1)
elif(opcao==3):
    print(num2)
elif(opcao==4):
    print(num3)
else:
    print("ERRO!")
    print("Por favor escolha a opção 2, 3 ou 4 ")
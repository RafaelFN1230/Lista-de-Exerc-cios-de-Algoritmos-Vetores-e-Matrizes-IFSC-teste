'''
Crie um algoritmo que peça o nome, a altura e o peso de duas pessoas e
apresente o nome e peso da mais pesada e o nome e altura da mais alta.
'''

nome1=input("Insira o nome: ")
peso1=float(input("Insira o peso: "))
altura1=float(input("Insira a altura: "))
nome2=input("Insira o nome: ")
peso2=float(input("Insira o peso: "))
altura2=float(input("Insira a altura: "))

if (peso1>peso2):
    print("Pessoa mais pessada.")
    print("Nome: ",nome1)
    print("Peso: ",peso1)
elif(peso2>peso1):
    print("Pessoa mais pessada.")
    print("Nome: ",nome2)
    print("Peso: ",peso2)

if(altura1>altura2):
    print("Pessoa mais pessada.")
    print("Nome: ",nome1)
    print("Altura: ",altura1)
if(altura2>altura1):
    print("Pessoa mais pessada.")
    print("Nome: ",nome2)
    print("Altura: ",altura2)